class Trie
{
    TrieNode root;
    public Trie()
    {
        root = new TrieNode();
    }
    public void add(String s)
    {
        TrieNode node = root;
        for(int i=0;i<s.length();i++)
        {
            TrieNode next = node.get(s.charAt(i));
            if(next == null)
            {
                node.add(s.charAt(i));
            }
            node = node.get(s.charAt(i));
        }
        node.setEnd();
    }
    public List<String> getStartWith(String s)
    {
        List<String> ans = new ArrayList();
        TrieNode node = root;
        for(int i=0;i<s.length();i++)
        {
            TrieNode next = node.get(s.charAt(i));
            if(next == null)
            {
                return ans;
            }
            node = node.get(s.charAt(i));
        }
        Deque<TrieNode> q = new ArrayDeque();
        Deque<String> sq = new ArrayDeque();
        q.addLast(node);
        sq.addLast(s);
        while(q.isEmpty() == false)
        {
            TrieNode top = q.pollFirst();
            String tillnow = sq.pollFirst();
            if(top.getEnd())
            {
                ans.add(tillnow);
            }
            for(int i=0;i<26;i++)
            {
                if(top.child[i] != null)
                {
                    q.addLast(top.child[i]);
                    sq.addLast(tillnow + (char)(i + 97));
                }
            }
        }
        Collections.sort(ans);
        if(ans.size() > 3)
        {
            return ans.subList(0,3);
        }
        else
        {
             return ans;
        }

    }
}
class TrieNode
{
    TrieNode[] child;
    boolean end;
    public TrieNode()
    {
        child = new TrieNode[26];
        end = false;
    }
    public void setEnd()
    {
        end = true;
    }
    public boolean getEnd()
    {
        return end;
    }
    public TrieNode get(char c)
    {
        return child[c - 97];
    }
    public void add(char c)
    {
        child[c - 97] = new TrieNode();
    }

}
class Solution {
    public List<List<String>> suggestedProducts(String[] products, String searchWord) {
        Trie t = new Trie();
        for(int i=0;i<products.length;i++)
        {
            String str = products[i];
            t.add(str);
        }
        List<List<String>> ans = new ArrayList();
        String s = "";
        for(int i=0;i<searchWord.length();i++)
        {
            s += searchWord.charAt(i);
            ans.add(t.getStartWith(s));
        }
        return ans;
    }
}