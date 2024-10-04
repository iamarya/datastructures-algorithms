<div _ngcontent-serverapp-c232="" class="note-body"><div _ngcontent-serverapp-c232="" class="body-text"><h3><strong>Python break statement</strong></h3><p>&nbsp;</p><p>The break statement terminates the loop containing it. Control of the program flows to the statement immediately after the body of the loop.</p><p>&nbsp;</p><p>If the break statement is inside a nested loop (loop inside another loop), the break statement will terminate the innermost loop.</p><p>&nbsp;</p><p><strong>Syntax:</strong></p><pre><code class="language-python hljs"><span class="hljs-keyword">break</span></code></pre><p>&nbsp;</p><p><strong>Example:</strong></p><pre><code class="language-python hljs">i = <span class="hljs-number">0</span>

<span class="hljs-keyword">while</span> i &lt; <span class="hljs-number">5</span>:
    <span class="hljs-keyword">if</span> i == <span class="hljs-number">3</span>:
        print(<span class="hljs-string">"Executing 'break' statement in the next statment and the flow of execution is being"</span>, end = <span class="hljs-string">" "</span>)
        <span class="hljs-keyword">break</span>
    
    print(i)
    i += <span class="hljs-number">1</span>
    
print(<span class="hljs-string">"shifted to here!"</span>)</code></pre><p>&nbsp;</p><p><strong>output:</strong></p><pre><code class="language-python hljs"><span class="hljs-number">0</span>
<span class="hljs-number">1</span>
<span class="hljs-number">2</span>
Executing <span class="hljs-string">'break'</span> statement <span class="hljs-keyword">in</span> the next statment <span class="hljs-keyword">and</span> the flow of execution <span class="hljs-keyword">is</span> being shifted to here!</code></pre><p>&nbsp;</p></div></div>