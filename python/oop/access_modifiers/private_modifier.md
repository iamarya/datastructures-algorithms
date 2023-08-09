<div _ngcontent-serverapp-c232="" class="note-body"><div _ngcontent-serverapp-c232="" class="body-text"><h2><strong>Private Modifier</strong></h2><p>&nbsp;</p><p>The members of a class that are declared <strong>private</strong> are accessible within the class only. A private access modifier is the most secure access modifier. Data members of a class are declared private by adding a double underscore ‘__’ symbol before the data member of that class. Consider the given example:</p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Student</span>:</span>
 &nbsp;&nbsp; 
 __name = <span class="hljs-literal">None</span> <span class="hljs-comment"># private member</span>
 age = <span class="hljs-literal">None</span> <span class="hljs-comment"># public member</span>
 &nbsp;&nbsp; 
 <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">__init__</span>(<span class="hljs-params">self, name, age</span>):</span> <span class="hljs-comment"># constructor</span>
 &nbsp;&nbsp;&nbsp;&nbsp;self.__name = name
 &nbsp;&nbsp;&nbsp;&nbsp;self.age = age
 
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<span class="hljs-comment">#Driver's code&nbsp;&nbsp;&nbsp;&nbsp; </span>
 &nbsp;&nbsp; 
obj = Student(<span class="hljs-string">"Boy"</span>, <span class="hljs-number">15</span>)
print(obj.age) <span class="hljs-comment">#calling a public member of the class</span>
print(obj.name) <span class="hljs-comment">#calling a private member of the class</span></code></pre><p><br>We will get the output as:</p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-number">10</span>
AttributeError: <span class="hljs-string">'Student'</span> object has no attribute <span class="hljs-string">'name'</span></code></pre><p>&nbsp;</p><p>We will get an <strong>AttributeError</strong> when we try to access the <strong>name</strong> attribute. This is because the<strong> name</strong> is a <strong>private</strong> attribute and hence it cannot be accessed from outside the class.</p><p><strong>Note</strong>: We can even have <strong>public</strong> and <strong>private</strong> methods.</p><p>&nbsp;</p><h2><strong>Private and Public modifiers with Inheritance</strong></h2><p>&nbsp;</p><p>&nbsp;&nbsp;&nbsp;&nbsp;● The subclass will be able to access any public method or instance attribute of</p><p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;the superclass.</p><p>&nbsp;&nbsp;&nbsp; ● The subclass will not be able to access any private method or instance attribute&nbsp;</p><p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; of the superclass.</p><p>&nbsp;</p></div></div>