<div _ngcontent-serverapp-c231="" class="note-body"><div _ngcontent-serverapp-c231="" class="body-text"><h2><strong>UserList</strong></h2><p>&nbsp;</p><p>The UserList class simulates a list in which the instance’s contents are kept in a regular list, which is accessible via the data attribute of UserList instances. The instance’s contents are initially set to a copy of the list, defaulting to the empty list []. The list can be iterable, for example, a real Python list or a UserList object.</p><p>UserList is a list-like container that acts as a wrapper around the list objects. This is useful when someone wants to create their own list with some modified or additional functionality.</p><p>&nbsp;</p><p><strong>Syntax:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">collections</span>.<span class="hljs-title">UserList</span>(<span class="hljs-params">[list]</span>)</span></code></pre><p>&nbsp;</p><p><strong>Example:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-comment"># Python program to demonstrate userlist </span>

<span class="hljs-keyword">from</span> collections <span class="hljs-keyword">import</span> UserList 

<span class="hljs-comment"># Creating a List where deletion is not allowed </span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyList</span>(<span class="hljs-params">UserList</span>):</span> 

  <span class="hljs-comment"># Function to stop deletion from List </span>
  <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">remove</span>(<span class="hljs-params">self, s = None</span>):</span> 
      <span class="hljs-keyword">raise</span> RuntimeError(<span class="hljs-string">"Deletion is not allowed"</span>) 

  <span class="hljs-comment"># Function to stop pop from List </span>
  <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">pop</span>(<span class="hljs-params">self, s = None</span>):</span> 
      <span class="hljs-keyword">raise</span> RuntimeError(<span class="hljs-string">"Deletion is not allowed"</span>) 
	
<span class="hljs-comment"># Driver's code </span>
L = MyList([<span class="hljs-string">'A'</span>, <span class="hljs-string">'B'</span>, <span class="hljs-string">'C'</span>, <span class="hljs-string">'D'</span>]) 

print(<span class="hljs-string">"Original List"</span>) 

<span class="hljs-comment"># Inserting to List o) </span>
print(L) 

<span class="hljs-comment"># Deliting From List </span>
L.remove() 
d.pop(<span class="hljs-string">'B'</span>)</code></pre><p>&nbsp;</p><p><strong>Output:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs">Original List                                                                                                             
After Insertion                                                                                                           
[<span class="hljs-string">'A'</span>, <span class="hljs-string">'B'</span>, <span class="hljs-string">'C'</span>, <span class="hljs-string">'D'</span>, <span class="hljs-string">'E'</span>]                                                                                                 
Traceback (most recent call last):                                                                                        
  File <span class="hljs-string">"main.py"</span>, line <span class="hljs-number">39</span>, <span class="hljs-keyword">in</span> &lt;module&gt;                                                                                    
    L.remove()                                                                                                            
  File <span class="hljs-string">"main.py"</span>, line <span class="hljs-number">22</span>, <span class="hljs-keyword">in</span> remove                                                                                      
    <span class="hljs-keyword">raise</span> RuntimeError(<span class="hljs-string">"Deletion is not allowed"</span>)                                                                         
RuntimeError: Deletion <span class="hljs-keyword">is</span> <span class="hljs-keyword">not</span> allowed </code></pre></div></div>