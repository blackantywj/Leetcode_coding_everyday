# My garbage code
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        resultlist = []
        resultlist = self.visitfunc(root, resultlist)
        return resultlist[1]
    
    def visitfunc(self, root, listresult):
        listmid = []
        if root.left != None:
            listmid_l = self.visitfunc(root.left, listresult)
        if root.right != None:
            listmid_r = self.visitfunc(root.right, listresult)
            # a, b = visitfunc(root.left), visitfunc(root.right)
        listresult.append(listmid_l[1], listmid_r[1])
        listmid.append(root.left, root.right)
        # listmid = a+b
        return listmid, listresult


# python code
def levelOrder(self, root):
    ans, level = [], [root]
    while root and level:
        ans.append([node.val for node in level])
        LRpair = [(node.left, node.right) for node in level]
        level = [leaf for LR in LRpair for leaf in LR if leaf] # God code
    return ans

def levelOrder(self, root):
    ans, level = [], [root]
    while root and level:
        ans.append([node.val for node in level])           
        level = [kid for n in level for kid in (n.left, n.right) if kid]
    return ans

def levelOrder(self, root):
    if not root:
        return []
    ans, level = [], [root]
    while level:
        ans.append([node.val for node in level])
        temp = []
        for node in level:
            temp.extend([node.left, node.right])
        level = [leaf for leaf in temp if leaf]
    return ans
