<div _ngcontent-serverapp-c232="" class="note-body"><div _ngcontent-serverapp-c232="" class="body-text"><h2><strong>Repeating/Replicating Strings</strong></h2><p>&nbsp;</p><p>You can use the<strong> *</strong> operator to replicate a string specified number of times. Consider the example given below:</p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-meta">&gt;&gt;&gt; </span>s= <span class="hljs-string">"Ninja"</span>
<span class="hljs-meta">&gt;&gt;&gt; </span>print(s*<span class="hljs-number">3</span>) <span class="hljs-comment">#s*3 will produce a new string with s repeated thrice</span>

NinjaNinjaNinja <span class="hljs-comment">#Output</span></code></pre><p>&nbsp;</p><p><strong>Note:</strong> You cannot use the <strong>*</strong> operator between two strings i.e. you cannot multiply a string by a different string.</p><p>&nbsp;</p><h2><strong>String Slicing in Python</strong></h2><p>&nbsp;</p><p>As the name suggests, Python slicing slices the string from the front to back to get a substring out of it.</p><p>&nbsp;</p><p>Python supports slicing through two methods:</p><ul><li>slice() Constructor</li><li>Extending Indexing</li></ul><p>&nbsp;</p><p><strong>slice() Constructor</strong></p><p>&nbsp;</p><p>The slice() constructor creates a slice object representing the set of indices specified by range(start, stop, step)</p><p>&nbsp;</p><p><strong>Syntax:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs">slice= &lt;String Name&gt;[StartIndex : StopIndex : Steps]</code></pre><pre><code class="language-python hljs">Syntax:

slice(stop)
slice(start, stop, step)

Parameters:
start: Starting index <span class="hljs-keyword">from</span> where we want the substring to start.
stop: Ending index where the substring needs to stop.
step: This <span class="hljs-keyword">is</span> an optional argument that signifies the jump between each selected index.

Return Type: Returns a sliced object containing elements <span class="hljs-keyword">in</span> the given range only.</code></pre><p>&nbsp;</p><p><strong>Example:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-comment"># Python program to demonstrate </span>
<span class="hljs-comment"># String slicing </span>

String =<span class="hljs-string">'CODINGNINJAS'</span>
<span class="hljs-comment"># Using slice constructor </span>
s1 = slice(<span class="hljs-number">5</span>) 
s2 = slice(<span class="hljs-number">1</span>, <span class="hljs-number">5</span>, <span class="hljs-number">2</span>) 
s3 = slice(<span class="hljs-number">-1</span>, <span class="hljs-number">-12</span>, <span class="hljs-number">-2</span>) 

print(<span class="hljs-string">"String slicing"</span>) 
print(String[s1]) 
print(String[s2]) 
print(String[s3])</code></pre><p>&nbsp;</p><p><strong>Output:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs">String slicing
CODIN
OI
SJIGIO</code></pre><p>&nbsp;</p><p><strong>Extending indexing</strong></p><p>&nbsp;</p><p>Python can also use the syntax for indexing in place of slice object. This is an easy way to slice a string both syntax-wise and execution-wise.</p><p>&nbsp;</p><p><strong>Syntax:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs">string[start:end:step]</code></pre><p>start, end, and step have the same mechanism as slice(), constructor.</p><p>&nbsp;</p><p><strong>Example:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-comment"># Python program to demonstrate </span>
<span class="hljs-comment"># string slicing </span>
<span class="hljs-comment"># String slicing </span>

String =<span class="hljs-string">'ASTRING'</span>
<span class="hljs-comment"># Using indexing sequence </span>
print(String[:<span class="hljs-number">3</span>]) 
print(String[<span class="hljs-number">1</span>:<span class="hljs-number">5</span>:<span class="hljs-number">2</span>]) 
print(String[<span class="hljs-number">-1</span>:<span class="hljs-number">-12</span>:<span class="hljs-number">-2</span>]) 

<span class="hljs-comment"># Prints string in reverse </span>
print(<span class="hljs-string">"\nReverse String"</span>) 
print(String[::<span class="hljs-number">-1</span>]) </code></pre><p>&nbsp;</p><p><strong>Output:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs">AST
SR
GITA
Reverse String
GNIRTSA
GITA</code></pre><h2>&nbsp;</h2><h2><strong>Comparing Strings</strong></h2><p>&nbsp;</p><p>&nbsp;</p><p>1.In string comparison, we aim to identify whether two strings are equivalent to each other and if not, which one is greater.</p><p>2.String comparison in Python takes place character by character i.e. each character in the same index, are compared with each other.</p><p>3.If the characters fulfill the given comparison condition, it moves to the characters in the next position. Otherwise, it merely returns&nbsp;<strong>False</strong>.</p><p>&nbsp;</p><p><strong>Note</strong>: Some points to remember when using string comparison operators:</p><p>&nbsp;</p><p>●The comparisons are&nbsp;<strong>case-sensitive</strong>, hence the<strong>&nbsp;same</strong>&nbsp;letters in different</p><p>letter cases(upper/lower) will be treated as different characters.</p><p>●If two characters are different, then their Unicode value is compared; the character with the smaller Unicode value is considered to be lower.</p><p>&nbsp;</p><p><strong>The following operators are used for comparison:</strong></p><p>&nbsp;</p><p>●&nbsp;<strong>==:</strong>&nbsp;&nbsp;checks whether two strings are equal</p><p>●&nbsp;<strong>!=:</strong>&nbsp;&nbsp;checks if two strings are not equal</p><p>●&nbsp;<strong>&lt;:</strong>&nbsp;&nbsp;checks if the left operand is smaller than the right.</p><p>●&nbsp;<strong>&gt;:</strong>&nbsp;&nbsp;checks if the right operand is smaller than the left operand.</p><p>●&nbsp;<strong>&lt;=:</strong>&nbsp;&nbsp;checks if the left operand is smaller than or equal to the right operand.</p><p>●&nbsp;<strong>&gt;=:</strong>&nbsp;checks if the right operand is smaller than or equal to the left operand.</p><p>&nbsp;</p><p><strong>Example:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs">print(<span class="hljs-string">"Ninja"</span> == <span class="hljs-string">"Ninja"</span>) 
print(<span class="hljs-string">"Ninja"</span> &lt; <span class="hljs-string">"Ninja"</span>) 
print(<span class="hljs-string">"Ninja"</span> &gt; <span class="hljs-string">"Ninja"</span>) 
print(<span class="hljs-string">"Ninja"</span> != <span class="hljs-string">"Ninja"</span>)</code></pre><p>&nbsp;</p><p><strong>Output:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-literal">True</span>
<span class="hljs-literal">False</span>
<span class="hljs-literal">False</span>
<span class="hljs-literal">False</span></code></pre><p>&nbsp;</p><p><strong>Using is and is not</strong></p><p>&nbsp;</p><p>The == operator checks if the value of both the left and right operands is the same or not whereas&nbsp;<strong>is</strong>&nbsp;operator checks if both the left and right operand refer to the same object. Similar explanation goes for != and&nbsp;<strong>is not</strong>.</p><p>Let us look at the following example:</p><p>&nbsp;</p><p><strong>Example:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs">str1 = <span class="hljs-string">"Ninja"</span>
str2 = <span class="hljs-string">"Ninja"</span>
str3 = str1 
  
print(<span class="hljs-string">"ID of str1 ="</span>, hex(id(str1))) 
print(<span class="hljs-string">"ID of str2 ="</span>, hex(id(str2))) 
print(<span class="hljs-string">"ID of str3 ="</span>, hex(id(str3))) 
print(str1 <span class="hljs-keyword">is</span> str1) 
print(str1 <span class="hljs-keyword">is</span> str2) 
print(str1 <span class="hljs-keyword">is</span> str3) 
  
str1 += <span class="hljs-string">"s"</span>
str4 = <span class="hljs-string">"Ninja"</span>
  
print(<span class="hljs-string">"\nID of changed str1 ="</span>, hex(id(str1))) 
print(<span class="hljs-string">"ID of str4 ="</span>, hex(id(str4))) 
print(str1 <span class="hljs-keyword">is</span> str4) </code></pre><p>&nbsp;</p><p><strong>Output:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs">ID of str1 = <span class="hljs-number">0x7fe6b544fdf0</span>
ID of str2 = <span class="hljs-number">0x7fe6b544fdf0</span>
ID of str3 = <span class="hljs-number">0x7fe6b544fdf0</span>
<span class="hljs-literal">True</span>
<span class="hljs-literal">True</span>
<span class="hljs-literal">True</span>
ID of changed str1 = <span class="hljs-number">0x7fe6b5417e30</span>
ID of str4 = <span class="hljs-number">0x7fe6b544fdf0</span>
<span class="hljs-literal">False</span></code></pre><p>&nbsp;</p><p>The object ID of the strings depends on the platform they are being checked and can vary for different machines. The object IDs of str1, str2, and str3 were the same; therefore, their comparison result is True in all the cases.</p><p>After the object id of str1 is changed, the comparison of str1 and str2 will be false. Even after creation of str4, which has the same contents as in the new str1, the comparison will still be false as their object IDs are different.</p></div></div>