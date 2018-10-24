import unittest

import hierarchysearch

from hierarchysearch import Body, BodyPart


class TestAddChildMethods(unittest.TestCase):
    def setUp(self):
        self.index_finger = BodyPart('Index Finger')
        self.ring_finger = BodyPart('Ring Finger')
        

    def test_add_child_on_constructor(self):
        self.arm = BodyPart('Arm', [self.index_finger, self.ring_finger])

        # checks if all children are added
        self.assertTrue(len(self.arm.children) == 2)
        self.assertTrue(self.arm.children[0] == self.index_finger)
        self.assertTrue(self.arm.children[1] == self.ring_finger)

    
    def test_add_child_dynamically(self):
        self.arm = BodyPart('Arm')
        self.arm.add_child(self.index_finger)
        self.arm.add_child(self.ring_finger)

        # checks if all children are added
        self.assertTrue(len(self.arm.children) == 2)
        self.assertTrue(self.arm.children[0] == self.index_finger)
        self.assertTrue(self.arm.children[1] == self.ring_finger)
    
    
class TestInitialBodyMethods(unittest.TestCase):
    INITIAL_STATE = ('[ ] Chest'
    + '\n\t[ ] Lungs'
    + '\n\t\t[ ] Right Lung'
    + '\n\t\t\t[ ] Superior Lobe'
    + '\n\t\t\t[ ] Middle Lobe'
    + '\n\t\t\t[ ] Inferior Lobe'
    + '\n\t\t[ ] Left Lung'
    + '\n\t\t\t[ ] Superior Lobe'
    + '\n\t\t\t[ ] Middle Lobe'
    + '\n\t[ ] Heart'
    + '\n\t\t[ ] Left Ventricle'
    + '\n\t\t[ ] Right Ventricle'
    + '\n\t\t[ ] Left Aorta'
    + '\n\t\t[ ] Right Aorta'
    + '\n\t\t[ ] Septum'
    )

    def setUp(self):
        self.body = hierarchysearch.initialize_body()


    def test_get_state(self):
        self.assertEqual(self.body.get_state(), self.INITIAL_STATE)


    def test_has_part(self):
        self.assertTrue(self.body.has_part('middle lobe'))



class TestSelectMethods(unittest.TestCase):

    ROOT_TEST = 'Chest'
    ALL_UPPER = ROOT_TEST.upper()
    ALL_LOWER = ROOT_TEST.lower()
    ONE_LEVEL_IN = 'Lungs'
    CHILD_UNDER_MULTIPLE_PARENTS = 'Superior Lobe'
    SPECIFIC_CHILD = ['Superior Lobe', 'left lung']
    NONEXISTENT_CHILD = 'Toes'

    ALL_DESELECTED = ('[ ] Chest'
    + '\n\t[ ] Lungs'
    + '\n\t\t[ ] Right Lung'
    + '\n\t\t\t[ ] Superior Lobe'
    + '\n\t\t\t[ ] Middle Lobe'
    + '\n\t\t\t[ ] Inferior Lobe'
    + '\n\t\t[ ] Left Lung'
    + '\n\t\t\t[ ] Superior Lobe'
    + '\n\t\t\t[ ] Middle Lobe'
    + '\n\t[ ] Heart'
    + '\n\t\t[ ] Left Ventricle'
    + '\n\t\t[ ] Right Ventricle'
    + '\n\t\t[ ] Left Aorta'
    + '\n\t\t[ ] Right Aorta'
    + '\n\t\t[ ] Septum'
    )

    SELECT_ROOT = ('[X] Chest'
    + '\n\t[ ] Lungs'
    + '\n\t\t[ ] Right Lung'
    + '\n\t\t\t[ ] Superior Lobe'
    + '\n\t\t\t[ ] Middle Lobe'
    + '\n\t\t\t[ ] Inferior Lobe'
    + '\n\t\t[ ] Left Lung'
    + '\n\t\t\t[ ] Superior Lobe'
    + '\n\t\t\t[ ] Middle Lobe'
    + '\n\t[ ] Heart'
    + '\n\t\t[ ] Left Ventricle'
    + '\n\t\t[ ] Right Ventricle'
    + '\n\t\t[ ] Left Aorta'
    + '\n\t\t[ ] Right Aorta'
    + '\n\t\t[ ] Septum'
    )

    SELECT_ONE_LEVEL_IN = ('[X] Chest'
    + '\n\t[X] Lungs'
    + '\n\t\t[ ] Right Lung'
    + '\n\t\t\t[ ] Superior Lobe'
    + '\n\t\t\t[ ] Middle Lobe'
    + '\n\t\t\t[ ] Inferior Lobe'
    + '\n\t\t[ ] Left Lung'
    + '\n\t\t\t[ ] Superior Lobe'
    + '\n\t\t\t[ ] Middle Lobe'
    + '\n\t[ ] Heart'
    + '\n\t\t[ ] Left Ventricle'
    + '\n\t\t[ ] Right Ventricle'
    + '\n\t\t[ ] Left Aorta'
    + '\n\t\t[ ] Right Aorta'
    + '\n\t\t[ ] Septum'
    )

    SELECT_CHILD = ('[X] Chest'
    + '\n\t[X] Lungs'
    + '\n\t\t[X] Right Lung'
    + '\n\t\t\t[X] Superior Lobe'
    + '\n\t\t\t[ ] Middle Lobe'
    + '\n\t\t\t[ ] Inferior Lobe'
    + '\n\t\t[X] Left Lung'
    + '\n\t\t\t[X] Superior Lobe'
    + '\n\t\t\t[ ] Middle Lobe'
    + '\n\t[ ] Heart'
    + '\n\t\t[ ] Left Ventricle'
    + '\n\t\t[ ] Right Ventricle'
    + '\n\t\t[ ] Left Aorta'
    + '\n\t\t[ ] Right Aorta'
    + '\n\t\t[ ] Septum'
    )

    SELECT_SPECIFIC_CHILD = ('[X] Chest'
    + '\n\t[X] Lungs'
    + '\n\t\t[ ] Right Lung'
    + '\n\t\t\t[ ] Superior Lobe'
    + '\n\t\t\t[ ] Middle Lobe'
    + '\n\t\t\t[ ] Inferior Lobe'
    + '\n\t\t[X] Left Lung'
    + '\n\t\t\t[X] Superior Lobe'
    + '\n\t\t\t[ ] Middle Lobe'
    + '\n\t[ ] Heart'
    + '\n\t\t[ ] Left Ventricle'
    + '\n\t\t[ ] Right Ventricle'
    + '\n\t\t[ ] Left Aorta'
    + '\n\t\t[ ] Right Aorta'
    + '\n\t\t[ ] Septum'
    )


    def setUp(self):
        self.body = hierarchysearch.initialize_body()
        

    def test_select_root(self):
        self.body.select(self.ROOT_TEST)
        self.assertEqual(self.body.get_state(), self.SELECT_ROOT)

    
    def test_select_all_uppercase(self):
        self.body.select(self.ALL_UPPER)
        self.assertEqual(self.body.get_state(), self.SELECT_ROOT)

    
    def test_select_all_lowercase(self):
        self.body.select(self.ALL_LOWER)
        self.assertEqual(self.body.get_state(), self.SELECT_ROOT)


    def test_select_child_one_level_in(self):
        self.body.select(self.ONE_LEVEL_IN)
        self.assertEqual(self.body.get_state(), self.SELECT_ONE_LEVEL_IN)


    def test_select_child_that_appears_under_multiple_parents(self):
        self.body.select(self.CHILD_UNDER_MULTIPLE_PARENTS)
        self.assertEqual(self.body.get_state(), self.SELECT_CHILD)


    def test_select_child_with_specific_parent(self):
        self.body.select(self.SPECIFIC_CHILD[0], self.SPECIFIC_CHILD[1])
        self.assertEqual(self.body.get_state(), 
                            self.SELECT_SPECIFIC_CHILD)


    def test_select_nonexistent_child(self):
        self.body.select(self.NONEXISTENT_CHILD)
        self.assertEqual(self.body.get_state(), self.ALL_DESELECTED)



class TestDeselectMethods(unittest.TestCase):
    ALL_UPPERCASE = "SEPTUM"
    CHILD_WITH_CHILDREN = 'Right Lung'
    CHILD_WITHOUT_CHILDREN = 'Inferior Lobe'
    CHILD_UNDER_MULTIPLE_PARENTS = 'Middle Lobe'
    SPECIFIC_CHILD = ['Superior Lobe', 'right lung']
    NONEXISTENT_CHILD = "Armpit"

    ALL_SELECTED = ('[X] Chest'
    + '\n\t[X] Lungs'
    + '\n\t\t[X] Right Lung'
    + '\n\t\t\t[X] Superior Lobe'
    + '\n\t\t\t[X] Middle Lobe'
    + '\n\t\t\t[X] Inferior Lobe'
    + '\n\t\t[X] Left Lung'
    + '\n\t\t\t[X] Superior Lobe'
    + '\n\t\t\t[X] Middle Lobe'
    + '\n\t[X] Heart'
    + '\n\t\t[X] Left Ventricle'
    + '\n\t\t[X] Right Ventricle'
    + '\n\t\t[X] Left Aorta'
    + '\n\t\t[X] Right Aorta'
    + '\n\t\t[X] Septum'
    )

    DESELECT_ALL_UPPER = ('[X] Chest'
    + '\n\t[X] Lungs'
    + '\n\t\t[X] Right Lung'
    + '\n\t\t\t[X] Superior Lobe'
    + '\n\t\t\t[X] Middle Lobe'
    + '\n\t\t\t[X] Inferior Lobe'
    + '\n\t\t[X] Left Lung'
    + '\n\t\t\t[X] Superior Lobe'
    + '\n\t\t\t[X] Middle Lobe'
    + '\n\t[X] Heart'
    + '\n\t\t[X] Left Ventricle'
    + '\n\t\t[X] Right Ventricle'
    + '\n\t\t[X] Left Aorta'
    + '\n\t\t[X] Right Aorta'
    + '\n\t\t[ ] Septum'
    )

    DESELECT_CHILD_WITH_CHILDREN = ('[X] Chest'
    + '\n\t[X] Lungs'
    + '\n\t\t[ ] Right Lung'
    + '\n\t\t\t[ ] Superior Lobe'
    + '\n\t\t\t[ ] Middle Lobe'
    + '\n\t\t\t[ ] Inferior Lobe'
    + '\n\t\t[X] Left Lung'
    + '\n\t\t\t[X] Superior Lobe'
    + '\n\t\t\t[X] Middle Lobe'
    + '\n\t[X] Heart'
    + '\n\t\t[X] Left Ventricle'
    + '\n\t\t[X] Right Ventricle'
    + '\n\t\t[X] Left Aorta'
    + '\n\t\t[X] Right Aorta'
    + '\n\t\t[X] Septum'
    )

    DESELECT_CHILD_WITHOUT_CHILDREN = ('[X] Chest'
    + '\n\t[X] Lungs'
    + '\n\t\t[X] Right Lung'
    + '\n\t\t\t[X] Superior Lobe'
    + '\n\t\t\t[X] Middle Lobe'
    + '\n\t\t\t[ ] Inferior Lobe'
    + '\n\t\t[X] Left Lung'
    + '\n\t\t\t[X] Superior Lobe'
    + '\n\t\t\t[X] Middle Lobe'
    + '\n\t[X] Heart'
    + '\n\t\t[X] Left Ventricle'
    + '\n\t\t[X] Right Ventricle'
    + '\n\t\t[X] Left Aorta'
    + '\n\t\t[X] Right Aorta'
    + '\n\t\t[X] Septum'
    )

    DESELECT_SPECIFIC_CHILD = ('[X] Chest'
    + '\n\t[X] Lungs'
    + '\n\t\t[X] Right Lung'
    + '\n\t\t\t[ ] Superior Lobe'
    + '\n\t\t\t[X] Middle Lobe'
    + '\n\t\t\t[X] Inferior Lobe'
    + '\n\t\t[X] Left Lung'
    + '\n\t\t\t[X] Superior Lobe'
    + '\n\t\t\t[X] Middle Lobe'
    + '\n\t[X] Heart'
    + '\n\t\t[X] Left Ventricle'
    + '\n\t\t[X] Right Ventricle'
    + '\n\t\t[X] Left Aorta'
    + '\n\t\t[X] Right Aorta'
    + '\n\t\t[X] Septum'
    )

    DESELECT_CHILD_WITH_MULTIPLE_INSTANCES = ('[X] Chest'
    + '\n\t[X] Lungs'
    + '\n\t\t[X] Right Lung'
    + '\n\t\t\t[X] Superior Lobe'
    + '\n\t\t\t[ ] Middle Lobe'
    + '\n\t\t\t[X] Inferior Lobe'
    + '\n\t\t[X] Left Lung'
    + '\n\t\t\t[X] Superior Lobe'
    + '\n\t\t\t[ ] Middle Lobe'
    + '\n\t[X] Heart'
    + '\n\t\t[X] Left Ventricle'
    + '\n\t\t[X] Right Ventricle'
    + '\n\t\t[X] Left Aorta'
    + '\n\t\t[X] Right Aorta'
    + '\n\t\t[X] Septum'
    )


    def setUp(self):
        self.body = hierarchysearch.initialize_body()
        self.body.select('superior lobe')
        self.body.select('inferior lobe')
        self.body.select('middle lobe')
        self.body.select('left ventricle')
        self.body.select('right ventricle')
        self.body.select('left aorta')
        self.body.select('right aorta')
        self.body.select('septum')


    def test_deselect_allupper(self):
        self.body.deselect(self.ALL_UPPERCASE)
        self.assertEqual(self.body.get_state(), self.DESELECT_ALL_UPPER)


    def test_deselect_child_with_children(self):
        self.body.deselect(self.CHILD_WITH_CHILDREN)
        self.assertEqual(self.body.get_state(), 
                            self.DESELECT_CHILD_WITH_CHILDREN)


    def test_deselect_child_without_children(self):
        self.body.deselect(self.CHILD_WITHOUT_CHILDREN)
        self.assertEqual(self.body.get_state(), 
                            self.DESELECT_CHILD_WITHOUT_CHILDREN)

    
    def test_deselect_child_with_specific_parent(self):
        self.body.deselect(self.SPECIFIC_CHILD[0], self.SPECIFIC_CHILD[1])
        self.assertEqual(self.body.get_state(),
                            self.DESELECT_SPECIFIC_CHILD)


    def test_deselect_child_that_appears_under_multiple_parents(self):
        self.body.deselect(self.CHILD_UNDER_MULTIPLE_PARENTS)
        self.assertEqual(self.body.get_state(), 
                            self.DESELECT_CHILD_WITH_MULTIPLE_INSTANCES)


    def test_deselect_nonexistent_child(self):
        self.body.select(self.NONEXISTENT_CHILD)
        self.assertEqual(self.body.get_state(), self.ALL_SELECTED)


if __name__ == '__main__':
    unittest.main()