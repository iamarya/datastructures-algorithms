<div _ngcontent-serverapp-c232="" class="note-body"><div _ngcontent-serverapp-c232="" class="body-text"><h2><strong>Polymorphism</strong></h2><p>&nbsp;</p><p>The literal meaning of polymorphism is the condition of occurrence in different forms. Polymorphism is a very important concept in programming. It refers to the use of a single type entity (method, operator, or object) to represent different types in different scenarios. Let's take a few examples:</p><p><br>&nbsp;</p><h3>&nbsp;<strong>Example 1: Polymorphism in addition(+) operator</strong></h3><p>&nbsp;</p><p>We know that the <strong>+</strong> operator is used extensively in Python programs. But, it does not have a single usage. For integer data types, the <strong>+</strong> operator is used to perform an arithmetic addition operation.</p><p>&nbsp;</p><pre><code class="language-python hljs">num1 = <span class="hljs-number">1</span> 
num2 = <span class="hljs-number">2</span> 
print(num1+num2)</code></pre><p>&nbsp;</p><p>Hence, the above program outputs <strong>3</strong>.</p><p>Similarly, for string data types, the <strong>+</strong> operator is used to perform concatenation</p><p>&nbsp;</p><pre><code class="language-python hljs">str1 = <span class="hljs-string">"Python"</span> 
str2 = <span class="hljs-string">"Programming"</span> 
print(str1+<span class="hljs-string">" "</span>+str2)</code></pre><p><br>As a result, the above program outputs <strong>"Python Programming"</strong>.</p><p>Here, we can see that a single operator + has been used to carry out different operations for distinct data types. This is one of the most simple occurrences of <strong>polymorphism</strong> in Python.</p><p>&nbsp;</p><h3><strong>Example 2: Functional Polymorphism in Python</strong>&nbsp;</h3><p>&nbsp;</p><p>There are some functions in Python which are compatible to run with multiple data types.</p><p>One such function is the len() function. It can run with many data types in Python. Let's look at some example use cases of the function</p><p>&nbsp;</p><pre><code class="language-python hljs">print(len(<span class="hljs-string">"abcdefgeh"</span>)) 
print(len([<span class="hljs-string">"a"</span>, <span class="hljs-string">"b"</span>, <span class="hljs-string">"c"</span>])) 
print(len({<span class="hljs-string">"a"</span>: <span class="hljs-number">1</span>, <span class="hljs-string">"b"</span>: <span class="hljs-number">2</span>}))</code></pre><p>&nbsp;</p><p><strong>output:</strong></p><pre><code class="language-python hljs"><span class="hljs-number">9</span>
<span class="hljs-number">3</span> 
<span class="hljs-number">2</span></code></pre><p>Here, we can see that many data types such as string, list, tuple, set, and dictionary can work with the <strong>len()</strong> function. However, we can see that it returns specific information(the length) about the specific data types.</p><h2>&nbsp;</h2><h2><strong>Class Polymorphism in Python</strong></h2><p>&nbsp;</p><p>Polymorphism is a very important concept in Object-Oriented Programming. We can use the concept of polymorphism while creating class methods as Python allows different classes to have methods with the same name.&nbsp;</p><p>We can then later generalize calling these methods by disregarding the object we are working with.&nbsp;</p><p>Let's look at an example:</p><p>&nbsp;</p><p><strong>Example 3: Polymorphism in Class Methods</strong></p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Male</span>:</span>
 &nbsp;&nbsp; 
 <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">__init__</span>(<span class="hljs-params">self, name, age</span>):</span>
 &nbsp;&nbsp;&nbsp;&nbsp;self.name = name
 &nbsp;&nbsp;&nbsp;&nbsp;self.age = age
 <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">info</span>(<span class="hljs-params">self</span>):</span>
 &nbsp;&nbsp;&nbsp;&nbsp;print(<span class="hljs-string">"Hi, I am Male"</span>)
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Female</span>:</span>
 &nbsp;&nbsp; 
 <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">__init__</span>(<span class="hljs-params">self, name, age</span>):</span>
 &nbsp;&nbsp;&nbsp;&nbsp;self.name = name
 &nbsp;&nbsp;&nbsp;&nbsp;self.age = age
 <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">info</span>(<span class="hljs-params">self</span>):</span>
 &nbsp;&nbsp;&nbsp;&nbsp;print(<span class="hljs-string">"Hi, I am Female"</span>)


<span class="hljs-comment">#Driver's code</span>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  
M = Male(<span class="hljs-string">"Sid"</span>, <span class="hljs-number">20</span>)
F = Female(<span class="hljs-string">"Zee"</span>,<span class="hljs-number">21</span>)
<span class="hljs-keyword">for</span> human <span class="hljs-keyword">in</span> (M, F): <span class="hljs-comment">#Run loop over the set of objects</span>
 &nbsp;&nbsp;human.info() <span class="hljs-comment">#call the info function common to both</span></code></pre><p>&nbsp;</p><p><strong>output:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs">Hi, I am Male 
Hi, I am Female</code></pre><p><br>Here, we have created two classes <strong>Male</strong> and <strong>Female</strong>. They share a similar structure and have the same method info(). However, notice that we have not created a common superclass or linked the classes together in any way. Even then, we can pack these two different objects into a tuple and iterate through them using a common <strong>human</strong> variable. It is possible due to <strong>polymorphism</strong>. We can call both the <strong>info()</strong> methods by just using <strong>human.info()</strong> call, where human is first M (Instance of Male) and then F (Instance of <strong>Female</strong>).</p><p>&nbsp;</p><h2><strong>Polymorphism and Inheritance</strong></h2><p>&nbsp;</p><p>Like in other programming languages, the child classes in Python also inherit methods and attributes from the parent class. We can redefine certain methods and attributes specifically to fit the child class, which is known as <strong>Method Overriding.</strong></p><p>&nbsp;</p><p>Polymorphism allows us to access these overridden methods and attributes that have the same name as the parent class. Let's look at an example:</p><p>&nbsp;</p><pre><code class="language-python hljs">
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Human</span>:</span>
 <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">__init__</span>(<span class="hljs-params">self, name</span>):</span>
 &nbsp;&nbsp;&nbsp;&nbsp;self.name = name
 <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">info</span>(<span class="hljs-params">self</span>):</span>
 &nbsp;&nbsp;&nbsp;&nbsp;print(“Hi, I am Human”)


<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Male</span>(<span class="hljs-params">Human</span>):</span>
 &nbsp;&nbsp; 
 <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">__init__</span>(<span class="hljs-params">self, name</span>):</span>
 &nbsp;&nbsp;&nbsp;&nbsp;super().__init__(name)
 <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">info</span>(<span class="hljs-params">self</span>):</span>
 &nbsp;&nbsp;&nbsp;&nbsp;print(“Hi, I am Male”)


<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Female</span>(<span class="hljs-params">Human</span>):</span>
 &nbsp;&nbsp; 
 <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">__init__</span>(<span class="hljs-params">self, name</span>):</span>
 &nbsp;&nbsp;&nbsp;&nbsp;super().__init__(name)
 <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">info</span>(<span class="hljs-params">self</span>):</span>
 &nbsp;&nbsp;&nbsp;&nbsp;print(“Hi, I am Female”)


<span class="hljs-comment">#Driver's code</span>

M = Male(“Sid”)
F = Female(“Zee”)
<span class="hljs-keyword">for</span> human <span class="hljs-keyword">in</span> (M, F): <span class="hljs-comment">#Run loop over the set of objects</span>
 &nbsp;&nbsp; human.info() <span class="hljs-comment">#call the info function common to both</span></code></pre><p>&nbsp;</p><p><strong>output:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs">Hi, I am Male 
Hi, I am Female</code></pre><p><br>Due to polymorphism, the Python interpreter automatically recognizes that the info() method for object M (<strong>Male</strong> class) is <strong>overridden</strong>. So, it uses the one defined in the subclass <strong>Male</strong>. Same with the object F (<strong>Female</strong> Class).&nbsp;</p><p><strong>Note: Method Overloading</strong>, a way to create multiple methods with the same name but different arguments, is not possible in Python.</p></div></div>