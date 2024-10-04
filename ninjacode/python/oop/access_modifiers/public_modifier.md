<div _ngcontent-serverapp-c232="" class="note-body"><div _ngcontent-serverapp-c232="" class="body-text"><h2><strong>Public Modifier</strong></h2><p>&nbsp;</p><p>The members of a class that are declared public are easily accessible from any part of the program. All data members and member functions of a class are public by default. Consider the given example:</p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Student</span>:</span>

 name = <span class="hljs-literal">None</span> <span class="hljs-comment"># public member by default</span>
 public age = <span class="hljs-literal">None</span> <span class="hljs-comment"># public member</span>
 
 <span class="hljs-comment"># constructor</span>
 <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">__init__</span>(<span class="hljs-params">self, name, age</span>):</span>
 &nbsp;&nbsp;&nbsp;&nbsp;self.name = name 
 &nbsp;&nbsp;&nbsp;&nbsp;self.age = age 


<span class="hljs-comment">#Driver's code</span>

obj = Student(<span class="hljs-string">"Boy"</span>, <span class="hljs-number">15</span>) 
print(obj.age) <span class="hljs-comment">#calling a public member of the class </span>
print(obj.name) <span class="hljs-comment">#calling a private member of the class</span></code></pre><p>&nbsp;</p><p>We will get the output as:</p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-number">15</span>
Boy</code></pre><p><br>We will be able to access both <strong>name</strong> and <strong>age</strong> of the object from outside the class as they are <strong>public</strong>. However, this is not a good practice due to security concerns.<br>&nbsp;</p></div></div>