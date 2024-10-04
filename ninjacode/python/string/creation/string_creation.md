<div _ngcontent-serverapp-c232="" class="note-body"><div _ngcontent-serverapp-c232="" class="body-text"><h2><strong>Introduction</strong></h2><p>&nbsp;</p><p>● A character is simply a symbol. For example, the English language has 26 characters;</p><p>while a string is a contiguous sequence of characters.</p><p>&nbsp;</p><p>● In Python, a string is a sequence of Unicode characters.</p><p>&nbsp;</p><p>● Python strings are immutable, which means they cannot be altered after they are created.</p><p>&nbsp;</p><p><strong>Note:</strong> Unicode was introduced to include every character in all languages and bring uniformity in encoding. You can learn more about Unicode from Python Unicode.</p><p>&nbsp;</p><p>Given below are some examples of Unicode Encoding</p><p>&nbsp;</p><pre><code class="language-python hljs">string =<span class="hljs-string">'pythön!'</span>→ Default UTF<span class="hljs-number">-8</span> Encoding: <span class="hljs-string">b'pyth\xc3\xb6n!'</span>
string =<span class="hljs-string">'python!'</span>→ Default UTF<span class="hljs-number">-8</span> Encoding: <span class="hljs-string">b'python!'</span></code></pre><p>&nbsp;</p><h2><strong>How to create a string in Python?</strong></h2><p>&nbsp;</p><p>Strings in Python can be created using single quotes, double quotes and even triple quotes.</p><p>&nbsp;</p><p><strong>Example:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-comment"># Defining strings in Python</span>

<span class="hljs-comment">#Using single quotes</span>
s1 = <span class="hljs-string">'Hello'</span>
print(s1)

<span class="hljs-comment">#Using double quotes</span>
s2 = <span class="hljs-string">"Hello"</span>
print(s2)

print(type(s1))
print(type(s2))</code></pre><p>&nbsp;</p><p><strong>Output:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs">Hello
Hello
&lt;<span class="hljs-class"><span class="hljs-keyword">class</span> '<span class="hljs-title">str</span>'&gt;
&lt;<span class="hljs-title">class</span> '<span class="hljs-title">str</span>'&gt;</span></code></pre><p>&nbsp;</p><p><strong>Note:</strong></p><p>We can use triple quotes to create docstrings and/or multiline strings.</p><p>&nbsp;</p><p><strong>Example:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs">s = <span class="hljs-string">'''
Hey, may name is Afzal
I am 27 years old.
I work as a Project Manager at Coding Ninjas.
'''</span>


<span class="hljs-comment">#Multiline string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
print(s)
</code></pre><p>&nbsp;</p><p><strong>Output:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs">Hey, may name <span class="hljs-keyword">is</span> Afzal
I am <span class="hljs-number">27</span> years old.
I work <span class="hljs-keyword">as</span> a Project Manager at Coding Ninjas.</code></pre><p>&nbsp;</p><p>If you wish to print a string in a new line you can use the new line character <strong>'\n'</strong>. This is used within the strings. For example:</p><p>&nbsp;</p><pre><code class="language-python hljs">print(<span class="hljs-string">'First line\nSecond line'</span>)</code></pre><p>&nbsp;</p><p>This would yield the result:</p><p>&nbsp;</p><pre><code class="language-python hljs">First Line
Second Line</code></pre><h2>&nbsp;</h2><h2><strong>Accessing Characters in a String</strong></h2><p>&nbsp;</p><p>String indices start at 0 and go on till 1 less than the length of the string. We can use the index operator [ ] to access a particular character in a string. Eg.</p><p><strong>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Index: &nbsp; &nbsp; &nbsp;0&nbsp; &nbsp; &nbsp;1&nbsp; &nbsp; &nbsp;2&nbsp; &nbsp; &nbsp;3 &nbsp; &nbsp; 4</strong></p><p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <strong>String "hello": &nbsp; &nbsp; &nbsp;h &nbsp; &nbsp; e &nbsp; &nbsp; l &nbsp; &nbsp; &nbsp;l &nbsp; &nbsp; &nbsp;o</strong></p><p>&nbsp;</p><p><strong>Note</strong>: Trying to access indexes out of the range (0, lengthOfString-1), will raise an <strong>IndexError</strong>. Also, the index must be an integer. We can't use float or other data types; this will result in <strong>TypeError</strong>.</p><p>&nbsp;</p><p>Let us take an example to understand how to access characters in a String:</p><p>&nbsp;</p><pre><code class="language-python hljs">s= <span class="hljs-string">"hello"</span>

print(s[<span class="hljs-number">0</span>]) <span class="hljs-comment">#Output: h</span>
print(s[<span class="hljs-number">2</span>]) <span class="hljs-comment">#Output: l</span>
print(s[<span class="hljs-number">4</span>]) <span class="hljs-comment">#Output: o</span></code></pre><h2>&nbsp;</h2><h2><strong>Negative Indexing</strong></h2><p>&nbsp;</p><p>Python allows negative indexing for strings. The index of <strong>-1</strong> refers to the last character, <strong>-2</strong> to the second last character,&nbsp; and so on. The negative indexing starts from the last character in the string.</p><p>&nbsp;</p><p><strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Positive Indexing:&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;0&nbsp; &nbsp; &nbsp;1&nbsp; &nbsp; &nbsp;2&nbsp; &nbsp; &nbsp;3 &nbsp; &nbsp; 4</strong></p><p><strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;String "hello": &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; h &nbsp; &nbsp; e &nbsp; &nbsp; &nbsp;l &nbsp; &nbsp; &nbsp;l &nbsp; &nbsp; o</strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</p><p><strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Negative Indexing:</strong>&nbsp; &nbsp; &nbsp;&nbsp;<strong> &nbsp; -5&nbsp; &nbsp; -4&nbsp; &nbsp; -3&nbsp; &nbsp; -2 &nbsp; -1</strong></p><p>&nbsp;</p><p>Let us take an example to understand how to access characters using negative indexing in a string:</p><p>&nbsp;</p><pre><code class="language-python hljs">s= <span class="hljs-string">"hello"</span>

print(s[<span class="hljs-number">-1</span>]) <span class="hljs-comment">#Output: 0</span>
print(s[<span class="hljs-number">-2</span>]) <span class="hljs-comment">#Output: l</span>
print(s[<span class="hljs-number">-3</span>]) <span class="hljs-comment">#Output: l</span></code></pre></div></div>