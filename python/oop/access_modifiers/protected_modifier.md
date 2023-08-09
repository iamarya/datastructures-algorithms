<div _ngcontent-serverapp-c232="" class="note-body"><div _ngcontent-serverapp-c232="" class="body-text"><h2><strong>Protected Modifier</strong></h2><p>&nbsp;</p><p>The members of a class that are declared protected are only accessible to a class derived from it. Data members of a class are declared <strong>protected</strong> by adding a single underscore ‘_’ symbol before the data member of that class. The given example will help you get a better understanding:</p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-comment"># superclass </span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Student</span>:</span>
  _name = <span class="hljs-literal">None</span> <span class="hljs-comment"># protected data member</span>
  
  <span class="hljs-comment"># constructor</span>
  <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">__init__</span>(<span class="hljs-params">self, name</span>):</span>
 &nbsp;&nbsp;&nbsp;&nbsp;self._name = name</code></pre><p><br>This is the parent class <strong>Student</strong> with a <strong>protected</strong> instance attribute <strong>_name</strong>. Now consider a subclass of this class:</p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Student</span>:</span>
    __name = <span class="hljs-literal">None</span> <span class="hljs-comment"># private member</span>
    age = <span class="hljs-literal">None</span> <span class="hljs-comment"># public member</span>
   
    <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">__init__</span>(<span class="hljs-params">self, name, age</span>):</span> <span class="hljs-comment"># constructor</span>
        self.__name = name
        self.age = age

<span class="hljs-comment">#Driver's code</span>
   
obj = Student(<span class="hljs-string">"Boy"</span>, <span class="hljs-number">15</span>)
print(obj.age) <span class="hljs-comment">#calling a public member of the class</span>
print(obj.name) <span class="hljs-comment">#calling a private member of the class</span>

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Display</span>(<span class="hljs-params">Student</span>):</span>
     <span class="hljs-comment"># constructor</span>
     <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">__init__</span>(<span class="hljs-params">self, name</span>):</span>
    	Student.__init__(self, name)
     
     <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">displayDetails</span>(<span class="hljs-params">self</span>):</span>
    	<span class="hljs-comment"># accessing protected data members of the superclass</span>
    	print(<span class="hljs-string">"Name: "</span>, self._name)

<span class="hljs-comment">#Driver's code   </span>
obj = Display(<span class="hljs-string">"Boy"</span>) <span class="hljs-comment"># creating objects of the derived class</span>
obj.displayDetails() <span class="hljs-comment"># calling public member functions of the class</span>
obj.name <span class="hljs-comment"># trying to access protected attribute</span></code></pre><p>&nbsp;</p><p>This class <strong>Display</strong> inherits the <strong>Student</strong> class. The method <strong>displayDetails()</strong> accesses the <strong>protected</strong> attribute <strong>_name</strong>. Further, we try to access it again outside this class.</p><p>&nbsp;</p><p><strong>output:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs">Name: Boy 
AttributeError: <span class="hljs-string">'Display'</span> object has no attribute <span class="hljs-string">'name'</span></code></pre><p>&nbsp;</p><p>You can observe that we were able to access the <strong>protected</strong> attribute <strong>_name</strong> from inside the <strong>displayDetails()</strong> method in the subclass. However, we were not able to access it outside the subclass and we got an <strong>AttributeError</strong>. This justifies the definition of the <strong>protected</strong> modifier.</p><p>&nbsp;</p><h3>Difference between private, protected, and public modifiers:</h3><p>&nbsp;</p><p>Let’s look at the summary of private, protected, and public access modifiers.</p><p>&nbsp;</p><figure class="table"><table><tbody><tr><td><strong>Visibility</strong></td><td><strong>Private</strong></td><td><strong>Protected</strong></td><td><strong>Public</strong></td></tr><tr><td>Within the same class</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>In derived Class</td><td>No</td><td>Yes</td><td>Yes</td></tr><tr><td>Outside the class</td><td>No</td><td>No</td><td>Yes</td></tr></tbody></table></figure><p><br>&nbsp;</p></div></div>