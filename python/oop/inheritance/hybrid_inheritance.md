<div _ngcontent-serverapp-c232="" class="note-body"><div _ngcontent-serverapp-c232="" class="body-text"><h2><strong>Hybrid Inheritance</strong></h2><p>&nbsp;</p><p>Hybrid inheritance is a combination of more than one type of inheritance. For example, A child and parent class relationship that follows multiple and hierarchical inheritances can be called hybrid inheritance.</p><p>&nbsp;</p><p><strong>Syntax:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Parent</span>:</span>
 &nbsp;&nbsp;&nbsp;<span class="hljs-keyword">pass</span>

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">child1</span>(<span class="hljs-params">Parent</span>):</span>
 &nbsp;&nbsp;&nbsp;<span class="hljs-keyword">pass</span>

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">child2</span>(<span class="hljs-params">Parent</span>):</span>
 &nbsp;&nbsp;&nbsp;<span class="hljs-keyword">pass</span>

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">child3</span>(<span class="hljs-params">child1,child2</span>):</span>
 &nbsp;&nbsp;&nbsp;<span class="hljs-keyword">pass</span></code></pre><p>&nbsp;</p><p><strong>Example:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-comment"># Python program to demonstrate</span>
<span class="hljs-comment"># hybrid inheritance</span>


<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">School</span>:</span>
<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">func1</span>(<span class="hljs-params">self</span>):</span>
	print(<span class="hljs-string">"This function is in school."</span>)


<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Student1</span>(<span class="hljs-params">School</span>):</span>
<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">func2</span>(<span class="hljs-params">self</span>):</span>
	print(<span class="hljs-string">"This function is in student 1. "</span>)


<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Student2</span>(<span class="hljs-params">School</span>):</span>
   <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">func3</span>(<span class="hljs-params">self</span>):</span>
	print(<span class="hljs-string">"This function is in student 2."</span>)


<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Student3</span>(<span class="hljs-params">Student1, School</span>):</span>
   <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">func4</span>(<span class="hljs-params">self</span>):</span>
	print(<span class="hljs-string">"This function is in student 3."</span>)


<span class="hljs-comment">#Driver's code</span>

object = Student3()
object.func1()
object.func2()</code></pre><p><br><strong>output:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs">This function <span class="hljs-keyword">is</span> <span class="hljs-keyword">in</span> school.
This function <span class="hljs-keyword">is</span> <span class="hljs-keyword">in</span> student <span class="hljs-number">1.</span></code></pre></div></div>