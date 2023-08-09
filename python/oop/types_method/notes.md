<div _ngcontent-serverapp-c232="" class="note-body"><div _ngcontent-serverapp-c232="" class="body-text"><h2><strong>Python Static Method</strong></h2><p>&nbsp;</p><p>Static methods, much like class methods, are methods that are bound to a class rather than its object.</p><p>They do not require a class instance creation. So, they are not dependent on the state of the object.</p><p>The difference between a static method and a class method is:</p><ul><li>The static method knows nothing about the class and just deals with the parameters.</li><li>The class method works with the class since its parameter is always the class itself.</li></ul><p>&nbsp;</p><p>Hence, in newer versions of Python, you can use the @staticmethod decorator.</p><p>&nbsp;</p><p><strong>Syntax:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-meta">@staticmethod</span>
<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">func</span>(<span class="hljs-params">args,..</span>):</span>
 &nbsp;&nbsp;&nbsp;<span class="hljs-keyword">pass</span></code></pre><p>&nbsp;</p><p><strong>Example:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Hello</span>:</span>
 &nbsp;&nbsp;&nbsp;<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">__init__</span>(<span class="hljs-params">self</span>):</span>
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="hljs-keyword">pass</span>
 &nbsp;&nbsp; 
 &nbsp;&nbsp;&nbsp;@staticmethod
 &nbsp;&nbsp;&nbsp;<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">printHello</span>():</span>
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print(<span class="hljs-string">"Hello World!"</span>)
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 
o = Hello()
o.printHello()</code></pre><p>&nbsp;</p><p><strong>output:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs">Hello World!</code></pre><p>&nbsp;</p><h2><strong>Python Instance Method</strong></h2><p>&nbsp;</p><p>Instance methods are the most common type of methods in Python classes. These are so-called because they can access the unique data of their instance. If you have two objects each created from a car class, then they each may have different properties. They may have different colors, engine sizes, seats, and so on.</p><p><br>Instance methods must have self as a parameter, but you don't need to pass this in every time. Self is another Python special term. Inside any instance method, you can use self to access any data or methods that may reside in your class. You won't be able to access them without going through self.</p><p><br>Finally, as instance methods are the most common, there's no decorator needed. Any method you create will automatically be created as an instance method unless you tell Python otherwise.</p><p>&nbsp;</p><p><strong>Example:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Student</span>:</span>
 &nbsp;&nbsp;&nbsp;name = “Parikh”
 &nbsp;&nbsp; 
 &nbsp;&nbsp;&nbsp;<span class="hljs-comment">#This is an instance method.</span>
 &nbsp;&nbsp;&nbsp;<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">store_details</span>(<span class="hljs-params">self</span>):</span>
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.age = <span class="hljs-number">60</span>


 &nbsp;&nbsp;&nbsp;<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">print_age</span>(<span class="hljs-params">self</span>):</span>
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print(self.age)

<span class="hljs-comment">#Driver's code</span>

s = Student()
s.store_details()
s.print_age()</code></pre><p>&nbsp;</p><p><strong>output:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-number">60</span></code></pre></div></div>