<div _ngcontent-serverapp-c231="" class="note-body"><div _ngcontent-serverapp-c231="" class="body-text"><h2><strong>Python Comments</strong></h2><p>&nbsp;</p><p>1. Comments can be used to explain Python code.</p><p>2. Comments can be used to make the code more readable.</p><p>3. Comments can be used to prevent execution when testing code.</p><p>&nbsp;</p><h2><strong>Creating a Comment</strong></h2><p>&nbsp;</p><p>Comments start with a '#', and Python will ignore them:</p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-comment"># This is a how we write a comment in python.</span>
print(<span class="hljs-string">"Hello, World!"</span>)</code></pre><p>&nbsp;</p><h2><strong>Multi-Line Comments</strong></h2><p>&nbsp;</p><p>Python does not really have a syntax for multi-line comments.</p><p>To add a multiline comment you could insert a '#' for each line:</p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-comment"># This way we can</span>
<span class="hljs-comment"># Write comments in </span>
<span class="hljs-comment"># Multiple lines. </span>
print(<span class="hljs-string">"Hello, World!"</span>)</code></pre><p>Or, not quite as intended, you can use a multiline string.</p><p>&nbsp;</p><p>Since Python will ignore string literals that are not assigned to a variable, you can add a multiline string (triple quotes) in your code, and place your comment inside it:</p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-string">"""
Another way to write
comments in more than one
Line.
"""</span>
print(<span class="hljs-string">"Hello, World!"</span>)</code></pre><p>&nbsp;</p><p><strong>Note: </strong>We can achieve multi-line comments by using single triple quotes or by double triple quotes.</p></div></div>