<div _ngcontent-serverapp-c232="" class="note-body"><div _ngcontent-serverapp-c232="" class="body-text"><h2><strong>Python Identity Operators</strong></h2><p>&nbsp;</p><p><strong>is</strong> and <strong>is not</strong> are the identity operators. It compares the reference id of the objects.</p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-keyword">is</span>&nbsp;         Returns true <span class="hljs-keyword">if</span> the operands are referring to the same object. 
<span class="hljs-keyword">is</span> <span class="hljs-keyword">not</span>&nbsp;     Returns true <span class="hljs-keyword">if</span> the operands are <span class="hljs-keyword">not</span> referring to the same object.</code></pre><p>&nbsp;</p><p><strong>Example:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-comment"># Examples of Identity operators </span>
a = <span class="hljs-number">10</span>
b = <span class="hljs-number">10</span>

name1 = <span class="hljs-string">'Coding Ninjas Studio'</span>
name2 = <span class="hljs-string">'Coding Ninjas Studio'</span>

list1 = [<span class="hljs-number">11</span>,<span class="hljs-number">22</span>,<span class="hljs-number">33</span>] 
list2 = [<span class="hljs-number">11</span>,<span class="hljs-number">22</span>,<span class="hljs-number">33</span>] 

print(a <span class="hljs-keyword">is</span> b) 
print(name1 <span class="hljs-keyword">is</span> <span class="hljs-keyword">not</span> name2) 

<span class="hljs-comment"># Output is False since lists are mutable. </span>
print(list1 <span class="hljs-keyword">is</span> list2) </code></pre><p>&nbsp;</p><p><strong>output</strong>:</p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-literal">True</span>
<span class="hljs-literal">False</span>
<span class="hljs-literal">False</span></code></pre></div></div>