<div _ngcontent-serverapp-c232="" class="note-body"><div _ngcontent-serverapp-c232="" class="body-text"><h2><strong>Python return statement</strong></h2><p>&nbsp;</p><p>A <strong>return</strong> statement is used to end the execution of the function call and returns the result (value of the expression following the return keyword) to the caller. The statements after the <strong>return</strong> statements are not executed. If the <strong>return</strong> statement is without any expression, then the special value None is returned.&nbsp;</p><p><br>&nbsp;</p><p><strong>Note:</strong> Return statement can not be used outside the function.</p><p><br><strong>Syntax:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">function</span>():</span>
 &nbsp;&nbsp;&nbsp;statements
 &nbsp;&nbsp; 
 &nbsp;&nbsp;&nbsp;<span class="hljs-keyword">return</span> [statement]</code></pre><p><br><strong>Example:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">fact</span>(<span class="hljs-params">n</span>):</span>
 &nbsp;&nbsp;&nbsp;fact = <span class="hljs-number">1</span>
 &nbsp;&nbsp;&nbsp;<span class="hljs-keyword">for</span> i <span class="hljs-keyword">in</span> range(<span class="hljs-number">1</span>,n+<span class="hljs-number">1</span>):
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;fact = fact * i
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 
 &nbsp;&nbsp;&nbsp;<span class="hljs-keyword">return</span> fact
 &nbsp;&nbsp; 
ans = fact(<span class="hljs-number">5</span>)
print(ans)</code></pre><p><br><strong>output:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-number">120</span></code></pre><p>&nbsp;</p><p><strong>Returning Multiple Values</strong></p><p><br><strong>Example:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">fun</span>():</span>


 &nbsp;&nbsp;&nbsp;a = <span class="hljs-number">2</span>
 &nbsp;&nbsp;&nbsp;b = <span class="hljs-number">3</span>
 &nbsp;&nbsp;&nbsp;<span class="hljs-keyword">return</span> a,b


a,b = fun()
print(a,b)</code></pre><p><br><strong>output:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-number">2</span> <span class="hljs-number">3</span></code></pre><p><br>&nbsp;</p></div></div>