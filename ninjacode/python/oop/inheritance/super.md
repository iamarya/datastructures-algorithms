<div _ngcontent-serverapp-c232="" class="note-body"><div _ngcontent-serverapp-c232="" class="body-text"><h2><strong>Python super()</strong></h2><p>&nbsp;</p><p>The super() built-in returns a proxy object (temporary object of the superclass) that allows us to access methods of the base class.</p><p>&nbsp;</p><p>In Python, super() has two major use cases:</p><p>&nbsp;</p><p>● Allows us to avoid using the base class name explicitly</p><p>● Working with Multiple Inheritance</p><p>&nbsp;</p><p><strong>Example:</strong></p><p>&nbsp;</p><p>In the case of single inheritance, it allows us to refer to the base class by super().</p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Mammal</span>(<span class="hljs-params">object</span>):</span>

 &nbsp;<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">__init__</span>(<span class="hljs-params">self, mammalName</span>):</span>
 &nbsp;&nbsp;&nbsp;print(mammalName, <span class="hljs-string">'is a warm-blooded animal.'</span>)
 &nbsp;&nbsp; 
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Dog</span>(<span class="hljs-params">Mammal</span>):</span>

 &nbsp;<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">__init__</span>(<span class="hljs-params">self</span>):</span>
 &nbsp;&nbsp;&nbsp;print(<span class="hljs-string">'Dog has four legs.'</span>)
 &nbsp;&nbsp;&nbsp;super().__init__(<span class="hljs-string">'Dog'</span>)
 &nbsp;&nbsp; 
d1 = Dog()</code></pre><p><br><strong>output:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs">Dog has four legs.
Dog <span class="hljs-keyword">is</span> a warm-blooded animal.</code></pre><p>&nbsp;</p><p>Here, we called the __init__() method of the Mammal class (from the Dog class) using code</p><p>&nbsp;</p><pre><code class="language-python hljs">super().__init__(<span class="hljs-string">'Dog'</span>)</code></pre><p>&nbsp;</p><p>instead of</p><p>&nbsp;</p><pre><code class="language-python hljs">Mammal.__init__(self, <span class="hljs-string">'Dog'</span>)</code></pre></div></div>