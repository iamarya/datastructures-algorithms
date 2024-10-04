<div _ngcontent-serverapp-c232="" class="note-body"><div _ngcontent-serverapp-c232="" class="body-text"><h2><strong>List Comprehension</strong></h2><p>&nbsp;</p><p>In Python, list comprehension is a powerful, elegant, and concise way to create a new list from an existing list.</p><p>A list comprehension consists of an expression followed by <strong>for</strong> statement inside square brackets.</p><p>&nbsp;</p><p><strong>Syntax:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs">newList = [<span class="hljs-string">'expression'</span> <span class="hljs-keyword">for</span> <span class="hljs-string">'item'</span> <span class="hljs-keyword">in</span> iterable] </code></pre><p>&nbsp;</p><p>Let's take an example when we are required to find '2 ^ i' for each ‘i’ from 0 to 9, list comprehension can be used as- &nbsp;</p><p>&nbsp;</p><p><strong>Example:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs">pow2 = [<span class="hljs-number">2</span> ** x <span class="hljs-keyword">for</span> x <span class="hljs-keyword">in</span> range(<span class="hljs-number">10</span>)]
print(pow2) </code></pre><p>&nbsp;</p><p><strong>Output:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs">[<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">4</span>, <span class="hljs-number">8</span>, <span class="hljs-number">16</span>, <span class="hljs-number">32</span>, <span class="hljs-number">64</span>, <span class="hljs-number">128</span>, <span class="hljs-number">256</span>, <span class="hljs-number">512</span>]</code></pre><p>&nbsp;</p><p>The above code is a simple one-line code for the below code.</p><p>&nbsp;</p><pre><code class="language-python hljs">pow2 = []
<span class="hljs-keyword">for</span> x <span class="hljs-keyword">in</span> range(<span class="hljs-number">10</span>):
 &nbsp;&nbsp;pow2.append(<span class="hljs-number">2</span> ** x)</code></pre><p>&nbsp;</p><p>Similarly, we can use other expressions to modify or create a new list.</p><p>&nbsp;</p><p><strong>Example:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs">newList = [x <span class="hljs-keyword">for</span> x <span class="hljs-keyword">in</span> range(<span class="hljs-number">10</span>) <span class="hljs-keyword">if</span> x % <span class="hljs-number">2</span> == <span class="hljs-number">1</span>]
print(newList)</code></pre><p>&nbsp;</p><p><strong>Output:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs">[<span class="hljs-number">1</span>, <span class="hljs-number">3</span>, <span class="hljs-number">5</span>, <span class="hljs-number">7</span>, <span class="hljs-number">9</span>]</code></pre></div></div>