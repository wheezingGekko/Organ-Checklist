import unittest

from hierarchysearch import initialize_body, parse_user_input
from hierarchysearch import Body, BodyPart

# try to mock things

# Tests to Create
#   If no root
#   If size of tree == 1
#   If tree has three children
#   If depth > 1
#   With the 'for the' format
#   
#   Each of this for the following:
#
#   initialize_body()
#       must assert if true
#
#   parse_user_input()
#       check if returning expected output
#
#   main()
#       check userinput for each instance
#           select
#           deselect
#           quit
#           enter
#           other


class TestFloatingMethods(unittest.TestCase):

    
    def test_initialize_body(self):
        pass

    
    def test_parse_user_input(self):
        pass


class TestSelectMethods(unittest.TestCase):


    ROOT_TEST = 'Chest'
    ALL_UPPER = ROOT_TEST.upper()
    ALL_LOWER = ROOT_TEST.lower()
    ONE_LEVEL_IN = 'Lungs'
    CHILD_UNDER_MULTIPLE_PARENTS = 'Superior Lobe'
    SPECIFIC_CHILD_UNDER_MULTIPLE_PARENTS = ('Superior Lobe of the ' + 
                                            'Left Lung')

    ALL_DESELECTED = ('[ ] Chest'
    + '\t[ ] Lungs'
    + '\t\t[ ] Right Lungs'
    + '\t\t\t[ ] Superior Lobe'
    + '\t\t\t[ ] Middle Lobe'
    + '\t\t\t[ ] Inferior Lobe'
    + '\t\t[ ] Left Lungs'
    + '\t[ ] Heart'
    + '\t\t[ ] Left Ventricle'
    + '\t\t[ ] Right Ventricle'
    + '\t\t[ ] Left Aorta'
    + '\t\t[ ] Right Aorta'
    + '\t\t[ ] Septum'
    )

    SELECT_ROOT = ('[X] Chest'
    + '\t[ ] Lungs'
    + '\t\t[ ] Right Lungs'
    + '\t\t\t[ ] Superior Lobe'
    + '\t\t\t[ ] Middle Lobe'
    + '\t\t\t[ ] Inferior Lobe'
    + '\t\t[ ] Left Lungs'
    + '\t[ ] Heart'
    + '\t\t[ ] Left Ventricle'
    + '\t\t[ ] Right Ventricle'
    + '\t\t[ ] Left Aorta'
    + '\t\t[ ] Right Aorta'
    + '\t\t[ ] Septum'
    )

    SELECT_ONE_LEVEL_IN = ('[X] Chest'
    + '\t[X] Lungs'
    + '\t\t[ ] Right Lungs'
    + '\t\t\t[ ] Superior Lobe'
    + '\t\t\t[ ] Middle Lobe'
    + '\t\t\t[ ] Inferior Lobe'
    + '\t\t[ ] Left Lungs'
    + '\t[ ] Heart'
    + '\t\t[ ] Left Ventricle'
    + '\t\t[ ] Right Ventricle'
    + '\t\t[ ] Left Aorta'
    + '\t\t[ ] Right Aorta'
    + '\t\t[ ] Septum'
    )

    SELECT_CHILD = ('[X] Chest'
    + '\t[X] Lungs'
    + '\t\t[X] Right Lung'
    + '\t\t\t[X] Superior Lobe'
    + '\t\t\t[ ] Middle Lobe'
    + '\t\t\t[ ] Inferior Lobe'
    + '\t\t[X] Left Lung'
    + '\t\t\t[X] Superior Lobe'
    + '\t\t\t[ ] Middle Lobe'
    + '\t[ ] Heart'
    + '\t\t[ ] Left Ventricle'
    + '\t\t[ ] Right Ventricle'
    + '\t\t[ ] Left Aorta'
    + '\t\t[ ] Right Aorta'
    + '\t\t[ ] Septum'
    )

    SELECT_SPECIFIC_CHILD = ('[X] Chest'
    + '\t[X] Lungs'
    + '\t\t[] Right Lung'
    + '\t\t\t[] Superior Lobe'
    + '\t\t\t[ ] Middle Lobe'
    + '\t\t\t[ ] Inferior Lobe'
    + '\t\t[X] Left Lung'
    + '\t\t\t[X] Superior Lobe'
    + '\t\t\t[ ] Middle Lobe'
    + '\t[ ] Heart'
    + '\t\t[ ] Left Ventricle'
    + '\t\t[ ] Right Ventricle'
    + '\t\t[ ] Left Aorta'
    + '\t\t[ ] Right Aorta'
    + '\t\t[ ] Septum'
    )


    def setUp(self):
        self.body = initialize_body()


    def test_select_root(self):
        self.body.select(self.ROOT_TEST)
        self.assertEquals(self.body.get_state(), self.SELECT_ROOT)

    
    def test_select_all_uppercase(self):
        self.body.select(self.ALL_UPPER)
        self.assertEquals(self.body.get_state(), self.SELECT_ROOT)

    
    def test_select_all_lowercase(self):
        self.body.select(self.ALL_LOWER)
        self.assertEquals(self.body.get_state(), self.SELECT_ROOT)


    def test_select_child_one_level_in(self):
        self.body.select(self.ONE_LEVEL_IN)
        self.assertEquals(self.body.get_state(), self.SELECT_ONE_LEVEL_IN)


    def test_select_child_that_appears_under_multiple_parents(self):
        self.body.select(self.CHILD_UNDER_MULTIPLE_PARENTS)
        self.assertEquals(self.body.get_state(), self.SELECT_CHILD)


    def test_select_child_with_specific_parent(self):
        self.body.select(self.SPECIFIC_CHILD_UNDER_MULTIPLE_PARENTS)
        self.assertEquals(self.body.get_state(), 
                            self.SELECT_SPECIFIC_CHILD)



class TestDeselectMethods(unittest.TestCase):

    ROOT_TEST = 'Chest'
    ALL_UPPER = ROOT_TEST.upper()
    ALL_LOWER = ROOT_TEST.lower()
    ONE_LEVEL_IN = 'Lungs'
    CHILD_UNDER_MULTIPLE_PARENTS = 'Superior Lobe'
    SPECIFIC_CHILD_UNDER_MULTIPLE_PARENTS = ('Superior Lobe of the ' + 
                                            'Left Lung')

    ALL_DESELECTED = ('[X] Chest'
    + '\t[X] Lungs'
    + '\t\t[X] Right Lungs'
    + '\t\t\t[X] Superior Lobe'
    + '\t\t\t[X] Middle Lobe'
    + '\t\t\t[X] Inferior Lobe'
    + '\t\t[X] Left Lungs'
    + '\t[X] Heart'
    + '\t\t[X] Left Ventricle'
    + '\t\t[X] Right Ventricle'
    + '\t\t[X] Left Aorta'
    + '\t\t[X] Right Aorta'
    + '\t\t[X] Septum'
    )

    DESELECT_CHILD_WITH_CHILDREN = ('[X] Chest'
    + '\t[X] Lungs'
    + '\t\t[X] Right Lungs'
    + '\t\t\t[X] Superior Lobe'
    + '\t\t\t[X] Middle Lobe'
    + '\t\t\t[X] Inferior Lobe'
    + '\t\t[X] Left Lungs'
    + '\t[X] Heart'
    + '\t\t[X] Left Ventricle'
    + '\t\t[X] Right Ventricle'
    + '\t\t[X] Left Aorta'
    + '\t\t[X] Right Aorta'
    + '\t\t[X] Septum'
    )

    DESELECT_CHILD_WITHOUT_CHILDREN = ('[X] Chest'
    + '\t[X] Lungs'
    + '\t\t[ ] Right Lungs'
    + '\t\t\t[ ] Superior Lobe'
    + '\t\t\t[ ] Middle Lobe'
    + '\t\t\t[ ] Inferior Lobe'
    + '\t\t[ ] Left Lungs'
    + '\t[ ] Heart'
    + '\t\t[ ] Left Ventricle'
    + '\t\t[ ] Right Ventricle'
    + '\t\t[ ] Left Aorta'
    + '\t\t[ ] Right Aorta'
    + '\t\t[ ] Septum'
    )

    DESELECT_SPECIFIC_CHILD = ('[X] Chest'
    + '\t[X] Lungs'
    + '\t\t[X] Right Lung'
    + '\t\t\t[X] Superior Lobe'
    + '\t\t\t[ ] Middle Lobe'
    + '\t\t\t[ ] Inferior Lobe'
    + '\t\t[X] Left Lung'
    + '\t\t\t[X] Superior Lobe'
    + '\t\t\t[ ] Middle Lobe'
    + '\t[ ] Heart'
    + '\t\t[ ] Left Ventricle'
    + '\t\t[ ] Right Ventricle'
    + '\t\t[ ] Left Aorta'
    + '\t\t[ ] Right Aorta'
    + '\t\t[ ] Septum'
    )

    DESELECT_CHILD_WITH_MULTIPLE_INSTANCES = ('[X] Chest'
    + '\t[X] Lungs'
    + '\t\t[] Right Lung'
    + '\t\t\t[] Superior Lobe'
    + '\t\t\t[ ] Middle Lobe'
    + '\t\t\t[ ] Inferior Lobe'
    + '\t\t[X] Left Lung'
    + '\t\t\t[X] Superior Lobe'
    + '\t\t\t[ ] Middle Lobe'
    + '\t[ ] Heart'
    + '\t\t[ ] Left Ventricle'
    + '\t\t[ ] Right Ventricle'
    + '\t\t[ ] Left Aorta'
    + '\t\t[ ] Right Aorta'
    + '\t\t[ ] Septum'
    )


    def setUp(self):
        self.body = initialize_body()
        self.body.select('superior lobe')
        self.body.select('inferior lobe')
        self.body.select('middle lobe lobe')
        self.body.select('left ventricle')
        self.body.select('right ventricle')
        self.body.select('left aorta')
        self.body.select('right aorta')


    def test_deselect_root(self):
        self.body.deselect(self.ROOT_TEST)
        self.assertEquals(self.body.get_state(), self.ALL_DESELECTED)

    
    def test_deselect_all_uppercase(self):
        self.body.deselect(self.ALL_UPPER)
        self.assertEquals(self.body.get_state(), self.SELECT_ROOT)

    
    def test_deselect_all_lowercase(self):
        self.body.deselect(self.ALL_LOWER)
        self.assertEquals(self.body.get_state(), self.SELECT_ROOT)


    def test_deselect_child_one_level_in(self):
        self.body.deselect(self.ONE_LEVEL_IN)
        self.assertEquals(self.body.get_state(), self.SELECT_ONE_LEVEL_IN)


    def test_deselect_child_that_appears_under_multiple_parents(self):
        self.body.deselect(self.CHILD_UNDER_MULTIPLE_PARENTS)
        self.assertEquals(self.body.get_state(), self.DESELECT_CHILD)



    def test_deselect_child_with_specific_parent(self):
        self.body.deselect(self.SPECIFIC_CHILD_UNDER_MULTIPLE_PARENTS)
        self.assertEquals(self.body.get_state(), 
                            self.DESELECT_SPECIFIC_CHILD)


class TestBodyPartMethods(unittest.TestCase):
    pass

    """ to be implemented
    def test_constructor(self):
        pass


    def test_add_internal(self):
        pass


    def test_select(self):
        pass


    def test_deselect(self):
        pass
    

    def test_print_state(self):
        pass


    def test_is_part(self):
        pass
    """


if __name__ == '__main__':
    unittest.main()