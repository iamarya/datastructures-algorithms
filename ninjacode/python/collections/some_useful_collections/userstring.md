<div _ngcontent-serverapp-c231="" class="note-body"><div _ngcontent-serverapp-c231="" class="body-text"><h2><strong>UserString</strong></h2><p>&nbsp;</p><p>User string is a string-like container and just like UserDict and UserList, it acts as a wrapper around string objects. It is used when someone wants to create their own strings with some modified or additional functionality.&nbsp;</p><p>&nbsp;</p><p><strong>Syntax:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">collections</span>.<span class="hljs-title">UserString</span>(<span class="hljs-params">seq</span>)</span></code></pre><p>&nbsp;</p><p><strong>Example:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-comment"># Python program to demonstrate </span>
<span class="hljs-comment"># userstring </span>


<span class="hljs-keyword">from</span> collections <span class="hljs-keyword">import</span> UserString 


<span class="hljs-comment"># Creating a Mutable String </span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Mystring</span>(<span class="hljs-params">UserString</span>):</span> 

   <span class="hljs-comment"># Function to append to </span>
   <span class="hljs-comment"># string </span>
   <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">append</span>(<span class="hljs-params">self, s</span>):</span> 
	 self.data += s 

   <span class="hljs-comment"># Function to rmeove from </span>
   <span class="hljs-comment"># string </span>
   <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">remove</span>(<span class="hljs-params">self, s</span>):</span> 
	 self.data = self.data.replace(s, <span class="hljs-string">""</span>) 


<span class="hljs-comment"># Driver's code </span>
s1 = Mystring(<span class="hljs-string">"Coding"</span>) 
print(<span class="hljs-string">"Original String:"</span>, s1.data) 

<span class="hljs-comment"># Appending to string </span>
s1.append(<span class="hljs-string">"n"</span>) 
print(<span class="hljs-string">"String After Appending:"</span>, s1.data) 

<span class="hljs-comment"># Removing from string </span>
s1.remove(<span class="hljs-string">"g"</span>) 
print(<span class="hljs-string">"String after Removing:"</span>, s1.data)</code></pre><p>&nbsp;</p><p><strong>Output:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs">Original String: Coding
String After Appending: Codingn
String after Removing: Codinn</code></pre></div></div>