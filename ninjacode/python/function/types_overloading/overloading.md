<div _ngcontent-serverapp-c232="" class="note-body"><div _ngcontent-serverapp-c232="" class="body-text"><h3><strong>Function Overloading:</strong>&nbsp;</h3><p>&nbsp;</p><p>As opposed to other languages (for example C++), method or function overloading is not supported in Python by default but that can be achieved in various ways.</p><p>&nbsp;</p><p>We can defined multiple functions with the same name but only the last function will be considered, all the rest gets hidden.</p><p>&nbsp;</p><p><strong>Example:</strong></p><p>&nbsp;</p><h4><strong>Method 1 (Not The Most Efficient Method):</strong></h4><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">mult</span>(<span class="hljs-params">a, b</span>):</span>
    print(a * b)
    
<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">mult</span>(<span class="hljs-params">a, b, c</span>):</span>
    
    print(a * b * c)
    
    
mult(<span class="hljs-number">2</span>, <span class="hljs-number">4</span>, <span class="hljs-number">3</span>)
mult(<span class="hljs-number">2</span>, <span class="hljs-number">7</span>)</code></pre><p>&nbsp;</p><p><strong>output:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-number">10</span> 
TypeError: mult() missing <span class="hljs-number">1</span> required positional argument: <span class="hljs-string">'c'</span></code></pre><p>&nbsp;</p><p>&nbsp;</p><p>In the above code, there are two mult() methods, but the python compiler can only see the last i.e the one with 3 parameters. Therefore, even though we can define multiple methods with the same name and different arguments, but only the last method of them can be used. Calling any of the other methods will produce an error. Like here calling will&nbsp;<strong>mult(2,3)</strong>&nbsp;an error.</p><p>&nbsp;</p><p>This issue can be overcomed by the following method:</p><p>&nbsp;</p><h4><strong>Method 2 (Efficient One):</strong></h4><p>By Using Multiple Dispatch Decorator&nbsp;</p><p>&nbsp;</p><p>Multiple Dispatch Decorator Can be installed by:&nbsp;</p><pre><code class="language-python hljs">pip3 install multipledispatch</code></pre><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-keyword">from</span> multipledispatch <span class="hljs-keyword">import</span> dispatch

<span class="hljs-meta">@dispatch(int,int)</span>
<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">mult</span>(<span class="hljs-params">a, b</span>):</span>
    print(a * b)
 &nbsp;&nbsp; 
<span class="hljs-meta">@dispatch(int,int,int)&nbsp;&nbsp;&nbsp; </span>
<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">mult</span>(<span class="hljs-params">a, b, c</span>):</span>
    print(a * b * c)
 &nbsp;&nbsp; 
 &nbsp;&nbsp; 
mult(<span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">5</span>)
mult(<span class="hljs-number">2</span>, <span class="hljs-number">3</span>)</code></pre><p>&nbsp;</p><p><strong>output:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-number">10</span> 
<span class="hljs-number">5</span></code></pre></div></div>