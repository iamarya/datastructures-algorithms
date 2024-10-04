<div _ngcontent-serverapp-c232="" class="note-body"><div _ngcontent-serverapp-c232="" class="body-text"><h3><strong>Python continue statement</strong></h3><p>&nbsp;</p><p>The continue statement in Python returns the control to the beginning of the while loop. The continue statement rejects all the remaining statements in the current iteration of the loop and moves the control back to the top of the loop.</p><p>&nbsp;</p><p>The continue statement can be used in both while and for loops.</p><p>&nbsp;</p><p><strong>Syntax:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-keyword">continue</span></code></pre><p>&nbsp;</p><p><strong>Example:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs">i = <span class="hljs-number">0</span>
<span class="hljs-keyword">while</span> i &lt; <span class="hljs-number">5</span>:

 &nbsp;&nbsp;&nbsp;<span class="hljs-keyword">if</span> i == <span class="hljs-number">3</span>:
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;i += <span class="hljs-number">1</span>
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="hljs-keyword">continue</span>
 &nbsp;&nbsp; 
 &nbsp;&nbsp;&nbsp;print(i)
 &nbsp;&nbsp;&nbsp;i += <span class="hljs-number">1</span></code></pre><p>&nbsp;</p><p><strong>output:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-number">0</span>
<span class="hljs-number">1</span>
<span class="hljs-number">2</span>
<span class="hljs-number">4</span></code></pre></div></div>