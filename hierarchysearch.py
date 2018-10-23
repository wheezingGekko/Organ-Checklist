"""
author: farrah shiela urmeneta
date: 10.22.18

checks off desired body parts/organs based on user input
also removes the check based on user input
"""


class Body(object):
    """ we treat the body like a tree-object containing branches/parts """
    def __init__(self, root):
        self.root = root


    def select(self, bodyPart):
        self.root.select(bodyPart)


    def deselect(self, bodyPart):
        self.root.deselect(bodyPart)


    def print_state(self):
        self.root.print_state(0)

    
    def has_part(self, bodyPart):
        return self.root.is_part(bodyPart)


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


    def add_internal(self, *bodyParts):
        """ dynamic method to add one child or multiple children """
        for i in range(len(bodyParts)):
            self.children.append(bodyParts[i])


    def get_part(self, bodyPart):
        """ checks if a body part exists given a string representing the 
        name of the body part. It is not case-sensitive
        """
        # if the body part in question is itself, then the body part
        # exists
        if bodyPart == self.name.lower():
            return self

        # otherwise, we check its children to see if they are the
        # body part we seek
        for part in self.children:
            # if one of the children are this part, then the body part
            # exists
            if part.is_part(bodyPart):
                return part

        # if we cannot find it, then it doesn't exist - perhaps
        # not in this branch
        return None


    def is_part(self, bodyPart):
        """ checks if a body part exists given a string representing the 
        name of the body part. It is not case-sensitive
        """
        # if the body part in question is itself, then the body part
        # exists
        if bodyPart == self.name.lower():
            return True

        # otherwise, we check its children to see if they are the
        # body part we seek
        for part in self.children:
            # if one of the children are this part, then the body part
            # exists
            if part.is_part(bodyPart):
                return True

        # if we cannot find it, then it doesn't exist - perhaps
        # not in this branch
        return False


    def select(self, bodyPart):
        """ selects the desired part, as well as all of its ancestors """
        # if this is the part, then we select it
        if bodyPart == self.name.lower():
            self.selected = True

        # it may not be the case that this is the desired part, so we then
        # look through its children to select that
        for part in self.children:
            # if its child has been selected, then it is also selected
            if (part.select(bodyPart) == True):
                self.selected = True

        return self.selected


    def deselect(self, bodyPart):
        """ deselects the desired part, as well as all of its children """
        # if this is the body part, then it deselects itself
        if self.name.lower() == bodyPart:
            self.selected = False
            # as well as its children
            for part in self.children:
                part.deselect(part.name.lower())
        else:
            # otherwise, it keeps searching through its children to
            # deselect the desired body part
            for part in self.children:
                part.deselect(bodyPart)


    def print_state(self, level):
        """ prints in a hierarchical fashion, where its level is denoted
        by the amount of tabs within its suffix
        """
        beginning = "\t" * level

        if self.selected:
            middle = "X"
        else:
            middle = " "

        print (beginning + "[" + middle + "] " + self.name)

        if self.children != []:
            for part in self.children:
                part.print_state(level + 1)
        

def intiaialize_body():
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
    heart.add_internal(BodyPart("Left Ventricle"))
    heart.add_internal(BodyPart("Right Ventricle"))
    heart.add_internal(BodyPart("Left Aorta"))
    heart.add_internal(BodyPart("Right Aorta"))
    heart.add_internal(BodyPart("Septum"))

    # preparing chest class
    chest = BodyPart("Chest", [lungs, heart])

    # the item to be manipulated
    return(Body(chest))


def parse_user_input(user_input):
    u_input_arr = user_input.split(" of the ")
    for i in u_input_arr:
        if i[:4] == "the ":
            i = i[4:]
    return u_input_arr


if __name__ == '__main__':
    
    body = intiaialize_body()

    QUIT_CMDS = ["q", "quit", "exit"]
    SELECT_CMDS = ["s", "select"]
    DESELECT_CMDS = ["d", "deselect"]

    while True:
        print ("\nThis is the current layout: \n")
        body.print_state()
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
            print("stems from a particular part, then enter:") 
            print("<part name> of the <parent part>; ex.") 
            print("the Superior Lobe of the Right Lung\n")
            print("This method can be stacked, ex.")
            print("Superior Lobe of the Right Lung of the Lungs\n")

            print("WARNING: CURRENTLY, YOU CAN ONLY SELECT AND DESELECT")
            print("ONE BODY PART AT A TIME. ATTEMPTING TO USE THE")
            print("'OF THE' FORM WILL RESULT IN UNEXPECTED BEHAVIORS\n")

            body_part_input = input("> ").lower()

            ## currently unfinished code for "of the" format
            '''
            body_part_input = parse_user_input(body_part_input)
            
            parts_exist = True

            for part in body_part_input:
                if not body.has_part(part):
                    print("That body part does not exist")
                    parts_exist = False
                    break
                    
            if parts_exist:
                action(body_part_input)
            '''

            if body.has_part(body_part_input):
                action(body_part_input)
            else:
                print("That body part does not exist")

        else:
            print("Please choose a valid command.")
            continue

