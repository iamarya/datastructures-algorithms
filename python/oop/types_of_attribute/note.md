<div _ngcontent-serverapp-c232="" class="note-body"><div _ngcontent-serverapp-c232="" class="body-text"><h2><strong>Instance Attributes</strong></h2><p>&nbsp;</p><p>Attributes created in <strong>​.__init__()</strong>​ are called <strong>​instance​</strong> attributes. An instance attribute’s value is specific to a particular instance of the class. All <strong>​Car​</strong> objects have a <strong>​name​</strong> and a <strong>t​opSpeed​</strong>, but the values for the <strong>name​</strong> and <strong>​topSpeed​</strong> attributes will vary depending on the <strong>Car​</strong> instance. Different objects of the <strong>​Car​</strong> class will have different names and top speeds.</p><p>&nbsp;</p><p><strong>Example:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Student</span>:</span>
 &nbsp;&nbsp;&nbsp;<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">__init__</span>(<span class="hljs-params">self,name,rollno</span>):</span>
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.name = name
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.rollno = rollno
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 
 &nbsp;&nbsp;&nbsp;<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">printDetails</span>(<span class="hljs-params">self</span>):</span>
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print(<span class="hljs-string">"name: "</span>,self.name)
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print(<span class="hljs-string">"rollno: "</span>,self.rollno)
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 
s = Student(<span class="hljs-string">"parikh"</span>,<span class="hljs-number">101</span>)
s.printDetails()</code></pre><p>&nbsp;</p><p><strong>output:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs">name:&nbsp; parikh
rollno:&nbsp; <span class="hljs-number">101</span></code></pre><h2><br>&nbsp;</h2><h2><strong>Class Attributes</strong></h2><p>&nbsp;</p><p>On the other hand, class attributes are attributes that have the same value for all class instances. You can define a class attribute by assigning a value to a variable name outside of<strong>.​ __init__()</strong>​.</p><p><br><strong>For example</strong>, the following <strong>​Car​</strong> class has a class attribute called <strong>color​</strong> with the value ​<strong>"Black"</strong>​:</p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-class"><span class="hljs-keyword">class</span>​ ​<span class="hljs-title">Car</span>​:</span>
 &nbsp;&nbsp;&nbsp;<span class="hljs-comment"># Class attribute</span>
 &nbsp;&nbsp;&nbsp;color = ​<span class="hljs-string">"Black"</span>


​&nbsp;   <span class="hljs-function"><span class="hljs-keyword">def</span>​ ​<span class="hljs-title">__init__</span>​(<span class="hljs-params">self, name, topSpeed</span>):</span>
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.name = name
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.topSpeed= topSpeed</code></pre><p><br>●&nbsp; Class attributes are defined directly beneath the first line of the class name and are indented by four spaces.</p><p>●&nbsp; They must always be assigned an initial value.</p><p>●&nbsp; When an instance of the class is created, the class attributes are automatically created and assigned to their initial values.</p><p>You should use class attributes to define properties that should have the same value for every class instance and you must use instance attributes for properties that vary from one instance to another.</p><p>Now that we have a Car​ class, let’s create some cars!</p><p><br><br>&nbsp;</p></div></div>