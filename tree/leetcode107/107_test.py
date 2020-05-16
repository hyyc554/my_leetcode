from tree.my_tree import Tree

def test_Suo():
   
    my_tree = Tree()
    my_tree.add(1)
    my_tree.add(2)
    my_tree.add(3)

    sul = Solution()
    res = sul.levelOrderBottom(my_tree)
    assert res == [[2,3],1]