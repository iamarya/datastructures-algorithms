<div _ngcontent-serverapp-c231="" class="note-body"><div _ngcontent-serverapp-c231="" class="body-text"><h2><strong>input()</strong></h2><p>&nbsp;</p><p>To take input from the user, we use the <strong>input()</strong> function.&nbsp;</p><p>&nbsp;</p><p><strong>input():</strong> This function first takes the input from the user and then evaluates the expression, which means Python automatically identifies whether the user entered a string or a number or list. If the input provided is not correct then either syntax error or exception is raised by python.</p><p>&nbsp;</p><p><strong>Example:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-comment"># Python program showing the use of input() </span>

val = input(<span class="hljs-string">"Enter your name: "</span>) 
print(val) </code></pre><p>&nbsp;</p><p><strong>Output:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs">Enter your name: saif
<span class="hljs-string">'saif'</span></code></pre><p>&nbsp;</p><h3><strong>How the input function works in Python :</strong></h3><ul><li>When the <strong>input()</strong> function executes, program flow will be stopped until the user has given input.</li><li>The text or message display on the output screen to ask a user to enter input value is optional i.e. the prompt, will be printed on the screen is optional.</li><li>Whatever you enter as input, the input function converts it into a string. if you enter an integer value still <strong>input()</strong> function convert it into a string. You need to explicitly convert it into an integer in your code using <strong>typecasting.</strong></li></ul><p>&nbsp;</p><p><strong>Example:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-comment"># Program to check input type in Python</span>
 
name = input (<span class="hljs-string">"Enter name :"</span>) 
print(name) 
<span class="hljs-keyword">print</span> (<span class="hljs-string">"type of name"</span>, type(name)) </code></pre><p>&nbsp;</p><p>Output:</p><pre><code class="language-plaintext hljs">Enter your name: saif
'saif' 
type of name &lt;class 'str'&gt;</code></pre><p>&nbsp;</p><p><strong>Example:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-comment"># Program to check input type in Python </span>

num = int(input (<span class="hljs-string">"Enter number :"</span>))
print(num) 
<span class="hljs-keyword">print</span> (<span class="hljs-string">"type of num"</span>, type(num)) </code></pre><p>&nbsp;</p><p><strong>Output:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs">Enter number : <span class="hljs-number">10</span>
<span class="hljs-number">10</span>
type of num &lt;<span class="hljs-class"><span class="hljs-keyword">class</span> '<span class="hljs-title">int</span>'&gt;</span></code></pre><p>&nbsp;</p><h2><strong>How to take space-separated input in one line in Python?</strong></h2><p>&nbsp;</p><pre><code class="language-python hljs">x, y = input().split() </code></pre><p>&nbsp;</p><p>Note that we don’t have to explicitly specify split(‘ ‘) because split() uses any whitespace characters as a delimiter as default.</p><p>One thing to note in the above Python code is, both x and y would be of string. We can convert them to int using another line</p><p>&nbsp;</p><p><strong>Example:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-comment"># Program take space-separated input in one line in Python</span>
 
x, y = input().split()
print(x, y) </code></pre><p>&nbsp;</p><p><strong>output:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-number">10</span> <span class="hljs-number">20</span>
<span class="hljs-number">10</span> <span class="hljs-number">20</span></code></pre><p>&nbsp;</p><p><strong>Example:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-comment"># Program to check input type in Python</span>
 
x, y = input().split()
a = input()
<span class="hljs-keyword">print</span> (<span class="hljs-string">"type of x"</span>, type(x))
<span class="hljs-keyword">print</span> (<span class="hljs-string">"type of y"</span>, type(y))
<span class="hljs-keyword">print</span> (<span class="hljs-string">"type of a"</span>, type(a))</code></pre><p>&nbsp;</p><p><strong>output:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-number">10</span> <span class="hljs-number">20</span>
Parikh
type of x &lt;<span class="hljs-class"><span class="hljs-keyword">class</span> '<span class="hljs-title">str</span>'&gt;
<span class="hljs-title">type</span> <span class="hljs-title">of</span> <span class="hljs-title">y</span> &lt;<span class="hljs-title">class</span> '<span class="hljs-title">str</span>'&gt;
<span class="hljs-title">type</span> <span class="hljs-title">of</span> <span class="hljs-title">a</span> &lt;<span class="hljs-title">class</span> '<span class="hljs-title">str</span>'&gt; </span></code></pre><p>&nbsp;</p><p><strong>Question: Add two numbers.</strong></p><p>&nbsp;</p><pre><code class="language-python hljs">print(<span class="hljs-string">"Enter the value of a"</span>)
a = int(input())
print(<span class="hljs-string">"Enter the value of b"</span>)
b = int(input())
c = a + b
print(<span class="hljs-string">"value of c is :"</span>, c)</code></pre><p>&nbsp;</p><p><strong>output:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs">Enter the value of a
<span class="hljs-number">2</span>
Enter the value of b
<span class="hljs-number">3</span>
value of c <span class="hljs-keyword">is</span> : <span class="hljs-number">5</span></code></pre><p>&nbsp;</p><p><strong>Example:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs">n = input()
print(n)
Input: Hello world
Output: <span class="hljs-string">'Hello World'</span></code></pre></div></div>