<div _ngcontent-serverapp-c231="" class="note-body"><div _ngcontent-serverapp-c231="" class="body-text"><h2><strong>OrderedDict</strong></h2><p>&nbsp;</p><p>Ordered dictionaries are similar to regular dictionaries with some extra capabilities relating to ordering operations.&nbsp;</p><p>An OrderedDict is also a sub-class of dictionary but unlike a dictionary, it remembers the order in which the keys were inserted.&nbsp;</p><p>They have become less important now that the built-in ‘dict’ class gained the ability to remember insertion order (but this new behaviour has become guaranteed only after Python 3.7).</p><p>&nbsp;</p><p><strong>Syntax:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">collections</span>.<span class="hljs-title">OrderedDict</span>()</span></code></pre><p>&nbsp;</p><p><strong>Example:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-comment"># A Python program to demonstrate working </span>
<span class="hljs-comment"># of OrderedDict </span>
<span class="hljs-keyword">from</span> collections <span class="hljs-keyword">import</span> OrderedDict 

print(<span class="hljs-string">"This is a standard python Dict:\n"</span>) 
d = {} 
d[<span class="hljs-string">'John'</span>] = <span class="hljs-number">1</span>
d[<span class="hljs-string">'Mary'</span>] = <span class="hljs-number">2</span>
d[<span class="hljs-string">'Lucy'</span>] = <span class="hljs-number">3</span>
d[<span class="hljs-string">'Brian'</span>] = <span class="hljs-number">4</span>
<span class="hljs-comment"># The order of the keys and values inserted won't be retained here</span>
<span class="hljs-keyword">for</span> key, value <span class="hljs-keyword">in</span> d.items(): 
	print(key, value) 

print(<span class="hljs-string">"\nThis is an Ordered Dict:\n"</span>) 
od = OrderedDict() 
od[<span class="hljs-string">'John'</span>] = <span class="hljs-number">1</span>
od[<span class="hljs-string">'Mary'</span>] = <span class="hljs-number">2</span>
od[<span class="hljs-string">'Lucy'</span>] = <span class="hljs-number">3</span>
od[<span class="hljs-string">'Brian'</span>] = <span class="hljs-number">4</span>
<span class="hljs-comment"># The order of the keys and values inserted would be preserved</span>
<span class="hljs-keyword">for</span> key, value <span class="hljs-keyword">in</span> od.items(): 
	print(key, value)</code></pre><p>&nbsp;</p><p><strong>Output:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs">This <span class="hljs-keyword">is</span> a standard python Dict:                                                                                                 
                                                                                                                                
Brian <span class="hljs-number">4</span>                                                                                                                         
Mary <span class="hljs-number">2</span>                                                                                                                          
John <span class="hljs-number">1</span>                                                                                                                          
Lucy <span class="hljs-number">3</span>                                                                                                                          
                                                                                                                                
This <span class="hljs-keyword">is</span> an Ordered Dict:                                                                                                        
                                                                                                                                
John <span class="hljs-number">1</span>                                                                                                                          
Mary <span class="hljs-number">2</span>                                                                                                                          
Lucy <span class="hljs-number">3</span>                                                                                                                          
Brian <span class="hljs-number">4</span></code></pre></div></div>