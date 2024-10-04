<div _ngcontent-serverapp-c231="" class="note-body"><div _ngcontent-serverapp-c231="" class="body-text"><h2><strong>Python Shortcuts and Tricks</strong></h2><p>&nbsp;</p><p><strong>Example:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-keyword">from</span> collections <span class="hljs-keyword">import</span> Counter

num_lst = [<span class="hljs-number">1</span>, <span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>, <span class="hljs-number">5</span>, <span class="hljs-number">3</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>, <span class="hljs-number">2</span>, <span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>]

cnt = Counter(num_lst)
print(dict(cnt))

<span class="hljs-comment"># first 2 most occurrence</span>
print(dict(cnt.most_common(<span class="hljs-number">2</span>)))
str_lst = [<span class="hljs-string">'blue'</span>, <span class="hljs-string">'red'</span>, <span class="hljs-string">'green'</span>, <span class="hljs-string">'blue'</span>, <span class="hljs-string">'red'</span>, <span class="hljs-string">'red'</span>, <span class="hljs-string">'green'</span>]

print(dict(Counter(str_lst)))</code></pre><p>&nbsp;</p><p><strong>Output:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs">{<span class="hljs-number">1</span>: <span class="hljs-number">3</span>, <span class="hljs-number">2</span>: <span class="hljs-number">4</span>, <span class="hljs-number">3</span>: <span class="hljs-number">4</span>, <span class="hljs-number">4</span>: <span class="hljs-number">2</span>, <span class="hljs-number">5</span>: <span class="hljs-number">1</span>}
{<span class="hljs-number">2</span>: <span class="hljs-number">4</span>, <span class="hljs-number">3</span>: <span class="hljs-number">4</span>}
{<span class="hljs-string">'blue'</span>: <span class="hljs-number">2</span>, <span class="hljs-string">'red'</span>: <span class="hljs-number">3</span>, <span class="hljs-string">'green'</span>: <span class="hljs-number">2</span>}</code></pre><h2>&nbsp;</h2><h2><strong>for loop Minimized</strong></h2><p>&nbsp;</p><p><strong>Example:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs">lst = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>]
doubled = []

<span class="hljs-keyword">for</span> num <span class="hljs-keyword">in</span> lst:
 &nbsp;&nbsp;doubled.append(num*<span class="hljs-number">2</span>)
print(doubled)

doubled = [num*<span class="hljs-number">2</span> <span class="hljs-keyword">for</span> num <span class="hljs-keyword">in</span> lst]
print(doubled)</code></pre><p>&nbsp;</p><p><strong>Output:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs">[<span class="hljs-number">2</span>, <span class="hljs-number">4</span>, <span class="hljs-number">6</span>]
[<span class="hljs-number">2</span>, <span class="hljs-number">4</span>, <span class="hljs-number">6</span>]</code></pre><h2>&nbsp;</h2><h2><strong>Check All Chars Uppercase</strong></h2><p>&nbsp;</p><p><strong>Example:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-keyword">import</span> string

<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">is_upper</span>(<span class="hljs-params">word</span>):</span>
 &nbsp;&nbsp;<span class="hljs-keyword">return</span> all(c <span class="hljs-keyword">in</span> string.ascii_uppercase <span class="hljs-keyword">for</span> c <span class="hljs-keyword">in</span> list(word))
 &nbsp;&nbsp;
print(is_upper(<span class="hljs-string">'HUMANBEING'</span>))
print(is_upper(<span class="hljs-string">'humanbeing'</span>))</code></pre><p>&nbsp;</p><p><strong>Output:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-literal">True</span>
<span class="hljs-literal">False</span></code></pre><h2>&nbsp;</h2><h2><strong>for and if in One Line</strong></h2><p>&nbsp;</p><p><strong>Example:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs">d = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">1</span>, <span class="hljs-number">3</span>]
a = [each <span class="hljs-keyword">for</span> each <span class="hljs-keyword">in</span> d <span class="hljs-keyword">if</span> each == <span class="hljs-number">1</span>]
print(a)</code></pre><p>&nbsp;</p><p><strong>Output:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs">[<span class="hljs-number">1</span>,<span class="hljs-number">1</span>]</code></pre><h2>&nbsp;</h2><h2><strong>Loop With Index</strong></h2><p>&nbsp;</p><p><strong>Example:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs">lst = [<span class="hljs-string">'a'</span>, <span class="hljs-string">'b'</span>, <span class="hljs-string">'c'</span>, <span class="hljs-string">'d'</span>]

<span class="hljs-keyword">for</span> index, value <span class="hljs-keyword">in</span> enumerate(lst):
 &nbsp;&nbsp;print(<span class="hljs-string">f"<span class="hljs-subst">{index}</span>, <span class="hljs-subst">{value}</span>"</span>)

<span class="hljs-keyword">for</span> index, value <span class="hljs-keyword">in</span> enumerate(lst, start=<span class="hljs-number">10</span>):
 &nbsp;&nbsp;print(<span class="hljs-string">f"<span class="hljs-subst">{index}</span>, <span class="hljs-subst">{value}</span>"</span>)</code></pre><p>&nbsp;</p><p><strong>Output:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-number">0</span>, a
<span class="hljs-number">1</span>, b
<span class="hljs-number">2</span>, c
<span class="hljs-number">3</span>, d
<span class="hljs-number">10</span>, a
<span class="hljs-number">11</span>, b
<span class="hljs-number">12</span>, c
<span class="hljs-number">13</span>, d</code></pre><h2>&nbsp;</h2><h2><strong>Reverse a String or List</strong></h2><p>&nbsp;</p><p><strong>Example:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs">a = <span class="hljs-string">"humanbeing"</span>
print(<span class="hljs-string">"Reversed :"</span>,a[::<span class="hljs-number">-1</span>])
b = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>, <span class="hljs-number">5</span>]
print(<span class="hljs-string">"Reversed :"</span>,b[::<span class="hljs-number">-1</span>])</code></pre><p>&nbsp;</p><p><strong>Output:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs">Reversed : gniebnamuh
Reversed : [<span class="hljs-number">5</span>, <span class="hljs-number">4</span>, <span class="hljs-number">3</span>, <span class="hljs-number">2</span>, <span class="hljs-number">1</span>]</code></pre><h2>&nbsp;</h2><h2><strong>Join String and List Together</strong></h2><p>&nbsp;</p><p><strong>Example:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs">str1 = <span class="hljs-string">"do"</span>
str2 = <span class="hljs-string">"more"</span>
lst = [<span class="hljs-string">"Write"</span>, <span class="hljs-string">"less"</span>, <span class="hljs-string">"code"</span>]
str3 = <span class="hljs-string">' '</span>.join(lst) + <span class="hljs-string">', '</span> + str1 + <span class="hljs-string">' '</span> + str2
print(str3)</code></pre><p>&nbsp;</p><p><strong>Output:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs">Write less code, do more</code></pre><h2>&nbsp;</h2><h2><strong>Convert List to Comma Separated String</strong></h2><p>&nbsp;</p><p><strong>Example:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs">fruits = [<span class="hljs-string">'apple'</span>, <span class="hljs-string">'mango'</span>, <span class="hljs-string">'orange'</span>]
print(<span class="hljs-string">', '</span>.join(fruits))

numbers = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>, <span class="hljs-number">5</span>]
print(<span class="hljs-string">', '</span>.join(map(str, numbers)))

items = [<span class="hljs-number">1</span>, <span class="hljs-string">'apple'</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-string">'orange'</span>]
print(<span class="hljs-string">', '</span>.join(map(str, items)))</code></pre><p>&nbsp;</p><p><strong>Output:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs">apple, mango, orange
<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>, <span class="hljs-number">5</span>
<span class="hljs-number">1</span>, apple, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, orange</code></pre><h2>&nbsp;</h2><h2><strong>Dictionary Get When Key Not Found</strong></h2><p>&nbsp;</p><p><strong>Example:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs">d = {<span class="hljs-string">'a'</span>: <span class="hljs-number">1</span>, <span class="hljs-string">'b'</span>: <span class="hljs-number">2</span>}
print(d.get(<span class="hljs-string">'c'</span>))
print(d.get(<span class="hljs-string">'c'</span>, <span class="hljs-number">3</span>))</code></pre><p>&nbsp;</p><p><strong>Output:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-literal">None</span>
<span class="hljs-number">3</span></code></pre><h2>&nbsp;</h2><h2><strong>Sort Dictionary</strong></h2><p>&nbsp;</p><p><strong>Example:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-keyword">from</span> operator <span class="hljs-keyword">import</span> itemgetter

d = {<span class="hljs-string">'a'</span>: <span class="hljs-number">10</span>, <span class="hljs-string">'b'</span>: <span class="hljs-number">20</span>, <span class="hljs-string">'c'</span>: <span class="hljs-number">5</span>, <span class="hljs-string">'d'</span>: <span class="hljs-number">8</span>, <span class="hljs-string">'e'</span>: <span class="hljs-number">5</span>}

<span class="hljs-comment"># sort by value</span>
print(sorted(d.items(), key=<span class="hljs-keyword">lambda</span> x: x[<span class="hljs-number">1</span>]))

<span class="hljs-comment"># sort by value</span>
print(sorted(d.items(), key=itemgetter(<span class="hljs-number">1</span>)))

<span class="hljs-comment"># sort by key</span>
print(sorted(d.items(), key=itemgetter(<span class="hljs-number">0</span>)))

<span class="hljs-comment"># sort by value and return keys</span>
print(sorted(d, key=d.get))</code></pre><p>&nbsp;</p><p><strong>Output:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs">[(<span class="hljs-string">'c'</span>, <span class="hljs-number">5</span>), (<span class="hljs-string">'e'</span>, <span class="hljs-number">5</span>), (<span class="hljs-string">'d'</span>, <span class="hljs-number">8</span>), (<span class="hljs-string">'a'</span>, <span class="hljs-number">10</span>), (<span class="hljs-string">'b'</span>, <span class="hljs-number">20</span>)]
[(<span class="hljs-string">'c'</span>, <span class="hljs-number">5</span>), (<span class="hljs-string">'e'</span>, <span class="hljs-number">5</span>), (<span class="hljs-string">'d'</span>, <span class="hljs-number">8</span>), (<span class="hljs-string">'a'</span>, <span class="hljs-number">10</span>), (<span class="hljs-string">'b'</span>, <span class="hljs-number">20</span>)]
[(<span class="hljs-string">'a'</span>, <span class="hljs-number">10</span>), (<span class="hljs-string">'b'</span>, <span class="hljs-number">20</span>), (<span class="hljs-string">'c'</span>, <span class="hljs-number">5</span>), (<span class="hljs-string">'d'</span>, <span class="hljs-number">8</span>), (<span class="hljs-string">'e'</span>, <span class="hljs-number">5</span>)]
[<span class="hljs-string">'c'</span>, <span class="hljs-string">'e'</span>, <span class="hljs-string">'d'</span>, <span class="hljs-string">'a'</span>, <span class="hljs-string">'b'</span>]</code></pre><h2>&nbsp;</h2><h2><strong>Swapping Values</strong></h2><p>&nbsp;</p><p><strong>Example:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs">a, b = <span class="hljs-number">9</span>, <span class="hljs-number">10</span>
a, b = b, a
print(a, b)</code></pre><p>&nbsp;</p><p><strong>Output:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-number">10</span>, <span class="hljs-number">9</span></code></pre><h2>&nbsp;</h2><h2><strong>Merge Dictionaries</strong></h2><p>&nbsp;</p><p><strong>Example:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs">d1 = {<span class="hljs-string">'a'</span>: <span class="hljs-number">1</span>}
d2 = {<span class="hljs-string">'b'</span>: <span class="hljs-number">2</span>}

print(dict(d1.items() | d2.items()))
print({**d1, **d2})

d1.update(d2)
print(d1)</code></pre><p>&nbsp;</p><p><strong>Output:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs">{<span class="hljs-string">'a'</span>: <span class="hljs-number">1</span>, <span class="hljs-string">'b'</span>: <span class="hljs-number">2</span>}
{<span class="hljs-string">'a'</span>: <span class="hljs-number">1</span>, <span class="hljs-string">'b'</span>: <span class="hljs-number">2</span>}
{<span class="hljs-string">'a'</span>: <span class="hljs-number">1</span>, <span class="hljs-string">'b'</span>: <span class="hljs-number">2</span>}</code></pre><h2>&nbsp;</h2><h2><strong>Easy Printing</strong></h2><p>&nbsp;</p><p><strong>Example:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs">row = [<span class="hljs-number">100</span>, <span class="hljs-string">"android"</span>, <span class="hljs-string">"ios"</span>, <span class="hljs-string">"blackberry"</span>]
print(<span class="hljs-string">', '</span>.join(str(x) <span class="hljs-keyword">for</span> x <span class="hljs-keyword">in</span> row))
print(*row, sep=<span class="hljs-string">', '</span>)</code></pre><p>&nbsp;</p><p><strong>Output:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-number">100</span>, android, ios, blackberry
<span class="hljs-number">100</span>, android, ios, blackberry</code></pre></div></div>