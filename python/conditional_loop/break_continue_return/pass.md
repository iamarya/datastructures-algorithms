<div _ngcontent-serverapp-c232="" class="note-body"><div _ngcontent-serverapp-c232="" class="body-text"><h3><strong>Python pass statement</strong></h3><p>&nbsp;</p><p>The <strong>pass</strong> statement is a null statement. But the difference between <strong>pass</strong> and comment is that comment is ignored by the interpreter whereas <strong>pass</strong> is not ignored.&nbsp;</p><p>&nbsp;</p><p>The <strong>pass</strong> statement is generally used as a placeholder i.e. when the user does not know what code to write. So user simply places <strong>pass</strong> at that line. Sometimes, <strong>pass</strong> is used when the user doesn’t want any code to execute. So user simply places <strong>pass</strong> there as empty code is not allowed in loops, function definitions, class definitions, or in if statements. So using <strong>pass</strong> statement user avoids this error.</p><p>&nbsp;</p><p><strong>Syntax:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-keyword">pass</span></code></pre><p>&nbsp;</p><p><strong>Example:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs">i = <span class="hljs-number">0</span>
<span class="hljs-keyword">while</span> i &lt; <span class="hljs-number">5</span>:
    <span class="hljs-keyword">if</span> i == <span class="hljs-number">3</span>:
        i += <span class="hljs-number">1</span>
        <span class="hljs-keyword">pass</span>
    
    <span class="hljs-keyword">else</span>:
        print(i)
        i += <span class="hljs-number">1</span></code></pre><p>&nbsp;</p><p><strong>output:</strong></p><pre><code class="language-python hljs"><span class="hljs-number">0</span>
<span class="hljs-number">1</span>
<span class="hljs-number">2</span>
<span class="hljs-number">4</span></code></pre></div></div>