<div _ngcontent-serverapp-c231="" class="note-body"><div _ngcontent-serverapp-c231="" class="body-text"><h2><strong>UserDict</strong></h2><p>&nbsp;</p><p>This class simulates a dictionary. The instance’s (contents) are kept in a regular dictionary, which is accessible via the data attribute of UserDict instances. If ‘initialdata’ is provided (which is the first parameter that a UserDict expects/takes), data is initialized with its contents; note that a reference to 'initialdata' will not be kept, allowing it to be used for other purposes.</p><p>UserDict is a dictionary-like container that acts as a wrapper around the dictionary objects. The need for this class has been partially supplanted by the ability to subclass directly from dict; however, this class can be easier to work with because the underlying dictionary is accessible as an attribute. This container is used when someone wants to create their own dictionary with some modified or new functionality.</p><p>&nbsp;</p><p><strong>Syntax:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">collections</span>.<span class="hljs-title">UserDict</span>(<span class="hljs-params">[initialdata]</span>)</span></code></pre><p>&nbsp;</p><p><strong>Example:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-comment"># Python program to demonstrate userdict </span>

<span class="hljs-keyword">from</span> collections <span class="hljs-keyword">import</span> UserDict 

<span class="hljs-comment"># Creating a Dictionary where deletion is not allowed </span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyDict</span>(<span class="hljs-params">UserDict</span>):</span> 

	<span class="hljs-comment"># Function to stop deletion from dictionary </span>
	<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">append</span>(<span class="hljs-params">self, val</span>):</span>
	    self.data.update(val)
	
	<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">__del__</span>(<span class="hljs-params">self</span>):</span> 
		<span class="hljs-keyword">raise</span> RuntimeError(<span class="hljs-string">"Cannot Delete elements"</span>) 

	<span class="hljs-comment"># Function to stop pop from dictionary </span>
	<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">pop</span>(<span class="hljs-params">self, s = None</span>):</span> 
		<span class="hljs-keyword">raise</span> RuntimeError(<span class="hljs-string">"Cannot Delete elements"</span>) 

	<span class="hljs-comment"># Function to stop popitem from Dictionary </span>
	<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">popitem</span>(<span class="hljs-params">self, s = None</span>):</span> 
		<span class="hljs-keyword">raise</span> RuntimeError(<span class="hljs-string">"Cannot Delete elements"</span>) 

<span class="hljs-comment"># Driver's code </span>
d = MyDict({<span class="hljs-string">'One'</span>:<span class="hljs-number">1</span>,<span class="hljs-string">'Two'</span>: <span class="hljs-number">2</span>,<span class="hljs-string">'Three'</span>: <span class="hljs-number">3</span>}) 

print(d.data)

d.append({<span class="hljs-string">'Four'</span>: <span class="hljs-number">4</span>})

print(d)

d.pop(<span class="hljs-string">'One'</span>)</code></pre><p>&nbsp;</p><p><strong>Output:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs">{<span class="hljs-string">'One'</span>: <span class="hljs-number">1</span>, <span class="hljs-string">'Three'</span>: <span class="hljs-number">3</span>, <span class="hljs-string">'Two'</span>: <span class="hljs-number">2</span>}                                                                                            
{<span class="hljs-string">'One'</span>: <span class="hljs-number">1</span>, <span class="hljs-string">'Three'</span>: <span class="hljs-number">3</span>, <span class="hljs-string">'Two'</span>: <span class="hljs-number">2</span>, <span class="hljs-string">'Four'</span>: <span class="hljs-number">4</span>}                                                                                 
Traceback (most recent call last):                                                                                          
  File <span class="hljs-string">"main.py"</span>, line <span class="hljs-number">47</span>, <span class="hljs-keyword">in</span> &lt;module&gt;                                                                                      
    d.pop(<span class="hljs-string">'One'</span>)                                                                                                            
  File <span class="hljs-string">"main.py"</span>, line <span class="hljs-number">31</span>, <span class="hljs-keyword">in</span> pop                                                                                           
    <span class="hljs-keyword">raise</span> RuntimeError(<span class="hljs-string">"Cannot Delete elements"</span>)                                                                            
RuntimeError: Cannot Delete elements                                                                                        
Exception ignored <span class="hljs-keyword">in</span>: &lt;bound method MyDict.__del__ of {<span class="hljs-string">'One'</span>: <span class="hljs-number">1</span>, <span class="hljs-string">'Three'</span>: <span class="hljs-number">3</span>, <span class="hljs-string">'Two'</span>: <span class="hljs-number">2</span>, <span class="hljs-string">'Four'</span>: <span class="hljs-number">4</span>}&gt;                          
Traceback (most recent call last):                                                                                          
  File <span class="hljs-string">"main.py"</span>, line <span class="hljs-number">26</span>, <span class="hljs-keyword">in</span> __del__                                                                                       
RuntimeError: Cannot Delete elements</code></pre></div></div>