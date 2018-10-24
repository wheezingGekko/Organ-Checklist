"""
author: farrah shiela urmeneta
date: 10.22.18

checks off desired body parts/organs based on user input
also removes the check based on user input

to-be-added:
    ability to stack parent specifics
    eg.
        superior lobe of the right lung of the lungs
"""


class Body(object):
    """ we treat the body like a tree-object containing branches/parts """
    def __init__(self, root):
        self.root = root


    def select(self, body_part, new_root=None):
        self.root.select(body_part, new_root)


    def deselect(self, body_part, new_root=None):
        self.root.deselect(body_part, new_root)

    
    def has_part(self, body_part, new_root=None):
        return self.root.is_part(body_part, new_root)


    def get_state(self):
        return self.root.get_state(0)


class BodyPart(object):
    """ each body part may have multiple branches, similar to a rose tree
    """
    def __init__(self, name, children=None):
        self.name = name
        self.selected = False
        if children is None:
            self.children = []
        else:
            self.children = children


    def __repr__(self):
        return self.name


    def add_child(self, *body_parts):
        """ dynamic method to add one child or multiple children """
        for i in range(len(body_parts)):
            self.children.append(body_parts[i])

    
    def _find_root(self, root):
        """ locates a part and returns it """
        if self.name.lower() == root:
            return self
        elif self.children == []:
            return None
        
        for part in self.children:
            if part._find_root(root) is not None:
                return part._find_root(root)


    def is_part(self, body_part, root=None):
        """ uses an internal method to check if the part is a child
        it can specify which part (if there are ones with repeating names)
        by specifying the desired root
        """
        # if there is a specified root, then we look for the body part there
        if root is not None:
            inner_root = self._find_root(root)
            return inner_root._inner_is_part(body_part)
        # else, we don't restrict the search and look everywhere
        else:
            return self._inner_is_part(body_part)


    def _inner_is_part(self, body_part):
        """ checks if a body part exists given a string representing the 
        name of the body part. It is not case-sensitive
        """
        # if the body part in question is itself, then the body part
        # exists
        if body_part == self.name.lower():
            return True

        # otherwise, we check its children to see if they are the
        # body part we seek
        for part in self.children:
            # if one of the children are this part, then the body part
            # exists
            if part.is_part(body_part):
                return True

        # if we cannot find it, then it doesn't exist - perhaps
        # not in this branch
        return False


    def select(self, body_part, root=None):
        """ uses an internal method to select a part and its ancestors,
        it can specify which part (if there are ones with repeating names)
        by specifying the desired root
        """
        # if we are looking for a specific body part, we search
        # where the root is
        if root is not None:
            inner_root = self._find_root(root)
            if inner_root.is_part(body_part):
                # we restrict the ancestor to the root for the particular
                # body part
                inner_root._inner_select(body_part)
                # then we select all of the ancestors up to that root
                self._inner_select(root)
        # otherwise we select everything with that body part name
        else:
            self._inner_select(body_part)


    def _inner_select(self, body_part):
        """ selects the desired part, as well as all of its ancestors """
        # if this is the part, then we select it
        if body_part == self.name.lower():
            self.selected = True

        # it may not be the case that this is the desired part, so we then
        # look through its children to select that
        for part in self.children:
            # if its child has been selected, then it is also selected
            if (part._inner_select(body_part) == True):
                self.selected = True

        return self.selected


    def deselect(self, body_part, root=None):
        """ uses an internal method to deselect a part and its children,
        it can specify which part (if there are ones with repeating names)
        by specifying the desired root
        """
        # if we are looking for a specific body part, we search
        # where the root is
        if root is not None:
            inner_root = self._find_root(root)
            # we restrict the ancestor to the root for the particular
            # body part
            inner_root._inner_deselect(body_part)
        # otherwise we deselect everything with that body part name
        else:
            self._inner_deselect(body_part)
        

    def _inner_deselect(self, body_part):
        """ deselects the desired part, as well as all of its children """
        # if this is the body part, then it deselects itself
        if body_part == self.name.lower():
            self.selected = False
            # as well as its children
            for part in self.children:
                part.deselect(part.name.lower())
        else:
            # otherwise, it keeps searching through its children to
            # deselect the desired body part
            for part in self.children:
                part.deselect(body_part)


    def get_state(self, level):
        """ prints in a hierarchical fashion, where its level is denoted
        by the amount of tabs within its suffix
        """
        beginning = "\t" * level

        if self.selected:
            middle = "X"
        else:
            middle = " "

        state =  (beginning + "[" + middle + "] " + self.name)

        if self.children != []:
            for part in self.children:
                state += "\n" + part.get_state(level + 1)

        return state
        

def initialize_body():
    """ instantiates body parts and initializes body """
    ## creating parts within lungs
    # right lung
    r_superior_lobe = BodyPart("Superior Lobe")
    r_middle_lobe = BodyPart("Middle Lobe")
    # left lung
    l_superior_lobe = BodyPart("Superior Lobe")
    l_middle_lobe = BodyPart("Middle Lobe")
    inferior_lobe = BodyPart("Inferior Lobe")

    # collecting said classes into respective lungs
    right_lung_internal = [r_superior_lobe, r_middle_lobe, inferior_lobe]
    left_lung_internal =  [l_superior_lobe, l_middle_lobe]

    # initialization of lungs
    right_lung = BodyPart("Right Lung", right_lung_internal)
    left_lung = BodyPart("Left Lung", left_lung_internal)
    lungs = BodyPart("Lungs", [left_lung, right_lung])

    # setting up parts within heart
    heart = BodyPart("Heart")
    heart.add_child(BodyPart("Left Ventricle"))
    heart.add_child(BodyPart("Right Ventricle"))
    heart.add_child(BodyPart("Left Aorta"))
    heart.add_child(BodyPart("Right Aorta"))
    heart.add_child(BodyPart("Septum"))

    # preparing chest class
    chest = BodyPart("Chest", [lungs, heart])

    # the item to be manipulated
    return Body(chest)


def parse_user_input(user_input):
    ''' separates user input by the "of the" string '''
    u_input_arr = user_input.split(" of the ")
    for i in u_input_arr:
        if i[:4] == "the ":
            i = i[4:]
    return u_input_arr


if __name__ == '__main__':

    QUIT_CMDS = ["q", "quit", "exit"]
    SELECT_CMDS = ["s", "select"]
    DESELECT_CMDS = ["d", "deselect"]

    body = initialize_body()
    
    while True:
        print ("\nThis is the current layout: \n")
        print(body.get_state())
        print ("\n")
        print ("What would you like to do?")
        print (""" 
        > (s)elect
        > (d)eselect
        > (q)uit
                """)
        user_input = input("> ").lower()

        if user_input in QUIT_CMDS:
            print("Good bye")
            break

        if user_input in SELECT_CMDS or user_input in DESELECT_CMDS:
            if user_input in SELECT_CMDS:
                action = body.select
            if user_input in DESELECT_CMDS:
                action = body.deselect

            print("\nPlease type your desired part.\n")
            print("In the case that you would like to choose a part that")
            print("stems from a particular parent, then enter:\n") 
            print("\t<part name> of the <parent part>")
            print("\tex. the Superior Lobe of the Right Lung\n")

            body_part_input = input("> ").lower()
            parts = parse_user_input(body_part_input)
            
            if len(parts) > 1 and body.has_part(parts[0], parts[1]):
                action(parts[0], parts[1])
            elif len(parts) == 1 and body.has_part(parts[0]):
                action(parts[0])
            else:
                print("\nThat body part does not exist!")
                
        else:
            print("Please choose a valid command.")

