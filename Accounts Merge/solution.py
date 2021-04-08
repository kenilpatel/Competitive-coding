class graph_node(object):
    def __init__(self,val,tp):
        self.val = val
        self.type = tp
        self.links = set()
    def add(self,new_node):
        self.links.add(new_node)
        
class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        emaild = defaultdict(lambda:None)
        for ac in accounts:
            name = ac[0]
            email = ac[1:]
            name_node = graph_node(name,'n')
            for e in email:
                email_node = emaild[e]
                if email_node == None:
                    email_node = graph_node(e,'e')
                email_node.add(name_node)
                emaild[e] = email_node
                name_node.add(email_node)
        ans = []
        visited = set()
        for ac in accounts:
            name = ac[0]
            email = ac[1]
            if emaild[email] not in visited:
                email_s = set()
                name_s = set()
                q = [emaild[email]]
                visited.add(q[0])
                while q:
                    top = q.pop(0)
                    if top.type == 'e':
                        email_s.add(top.val)
                    else:
                        name_s.add(top.val)
                    for l in top.links:
                        if l not in visited:
                            visited.add(l)
                            q.append(l)
                local_ans = [name] + sorted(list(email_s))
                ans.append(local_ans)
        return ans

                
                
            
