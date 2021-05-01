class TrieNode
{
    TrieNode child[];
    boolean end;
    public TrieNode()
    {
        this.child = new TrieNode[26];
        this.end = false;
    }
    public boolean getEnd()
    {
        return this.end;
    }
    public void setEnd()
    {
        this.end = true;
    }
    public TrieNode get(char c)
    {
        int pos = c - 97;
        return this.child[pos];
    }
    public void add(char c)
    {
        int pos = c - 97;
        this.child[pos] = new TrieNode();
    }


}
class MapSum {

    TrieNode root;
    Map<String,Integer> map;
    public MapSum() {
        this.root = new TrieNode();
        this.map = new HashMap<String,Integer>();
    }

    public void insert(String key, int val) {
        this.map.put(key,val);
        TrieNode node = this.root;
        for(int i = 0;i<key.length();i++)
        {
            char c = key.charAt(i);
            TrieNode temp = node.get(c);
            if(temp == null)
            {
                node.add(c);
                node = node.get(c);
            }
            else
            {
                node = temp;
            }
        }
        node.setEnd();

    }

    public int sum(String prefix) {
        int sum = 0;
        TrieNode node = this.root;
        for(int i=0;i<prefix.length();i++)
        {
            char c = prefix.charAt(i);
            TrieNode temp = node.get(c);
            if(temp == null)
            {
                return sum;
            }
            else
            {
                node = temp;
            }
        }
        if(node == null)
        {
            return sum;
        }
        Deque<TrieNode> q = new ArrayDeque<TrieNode>();
        Deque<String> str = new ArrayDeque<String>();
        q.addLast(node);
        str.addLast(prefix);
        while(q.size() > 0)
        {
            TrieNode top = q.pollFirst();

            String st = str.pollFirst();
            if(top.getEnd())
            {
                sum += this.map.getOrDefault(st,0);
            }


            for(int i=0;i<26;i++)
            {
                char c = (char)(i + 97);
                TrieNode temp = top.get(c);
                if(temp != null)
                {
                    q.addLast(temp);
                    String new_s= new String(st);
                    new_s += c;
                    str.addLast(new_s);
                }
            }
        }
        return sum;
    }
}