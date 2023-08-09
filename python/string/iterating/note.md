<div _ngcontent-serverapp-c232="" class="note-body"><div _ngcontent-serverapp-c232="" class="body-text"><h2><strong>Iterating On Strings</strong></h2><p>&nbsp;</p><p>There are multiple ways to iterate over a string in Python.</p><p>&nbsp;</p><h3><strong>Using for loop</strong></h3><p>&nbsp;</p><p><strong>Example:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs">s = <span class="hljs-string">"MdAzmatAli"</span>

<span class="hljs-comment"># Using for loop</span>
<span class="hljs-keyword">for</span> i <span class="hljs-keyword">in</span> s:
 &nbsp;&nbsp;&nbsp;print(i) <span class="hljs-comment">#Print the character in the string</span></code></pre><p>&nbsp;</p><p><strong>Output:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs">M
d
A
z
m
a
t
A
l
i</code></pre><h3>&nbsp;</h3><h3><strong>Using for loop and range()</strong></h3><p>&nbsp;</p><p><strong>Example:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs">s = <span class="hljs-string">"MdAzmatAli"</span>

<span class="hljs-comment"># Using for loop</span>
<span class="hljs-keyword">for</span> i <span class="hljs-keyword">in</span> range(len(s)):
 &nbsp;&nbsp;&nbsp;print(s[i]) <span class="hljs-comment">#Print the character in the string</span></code></pre><p>&nbsp;</p><p><strong>Output:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs">M
d
A
z
m
a
t
A
l
i</code></pre><p><strong>Note: You can even use while() loops. Try using the while() loops on your own.</strong></p></div></div>