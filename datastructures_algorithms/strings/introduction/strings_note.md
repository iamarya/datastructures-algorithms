<div _ngcontent-serverapp-c231="" class="body-text">
    <h2><strong>Introduction to strings</strong></h2>
    <p>&nbsp;</p>
    <p>A string is a data type in programming that is defined as a sequence of <strong>characters</strong>, it is
        implemented as an array of bytes (or words) that stores a sequence of elements, typically characters using some
        character encoding.</p>
    <p>Depending on the programming language, strings can be of two types:</p>
    <ul>
        <li><strong>Mutable strings:</strong> Mutable strings are strings that can be modified. However, it depends on
            the declaration and the programming language.</li>
        <li><strong>Immutable strings: Immutable strings are strings that cannot be modified, the string is unique.
                Making any changes to the string involves creating a copy of the original string and deallocating
                it.</strong></li>
    </ul>
    <h2><strong>Operations on strings</strong></h2>
    <p>&nbsp;</p>
    <p>Common string operations include finding the <strong>length</strong>,<strong> copying</strong>,<strong>
            concatenating</strong>, <strong>replacing</strong>, <strong>counting</strong> the occurrences of characters
        in a string. Such operations on strings can be performed easily with built-in functions provided by any
        programming language.</p>
    <p>&nbsp;</p>
    <p>Some of the standard operations involving strings:&nbsp;</p>
    <ul>
        <li><strong>Access characters:</strong> Retrieving characters of the string. Similar to arrays, strings follow
            0-based indexing. For example, S = “apple”, ‘a’ is the character at 0th index ( S[0] ), ‘e’ is the character
            at 4th index of the string S ( S[4] ).</li>
        <li><strong>Concatenation:</strong> Joining characters end to end, combining strings.For example: &nbsp;S1 =
            “Hello ”, S2 = “World.”, the concatenation of strings S1 and S2 represented by S3 is S3 = S1+S2 =&gt; “Hello
            World.” , while S3 = S2+S1 =&gt; “World.Hello ”.</li>
        <li><strong>Substring:</strong> A contiguous sequence of characters in a string. For example, Substrings of the
            string “boy” are: “”, ”b”, ”o”, ”y”, ”bo”, ”oy”, ”boy” ( an empty string is also a substring ).<ul>
                <li><strong>Prefix:</strong> A prefix is any leading contiguous part of the string. For example, S =
                    “garden” - “”, “g”, ”ga”, ”gar”, ”gard”, ”garde”,&nbsp; “garden” are all prefixes of the string S.
                </li>
                <li><strong>Suffix:</strong> A suffix is any trailing contiguous part of the string. For example, S =
                    “garden” - “”, ”n”, ”en”, ”den”, ”rden”, ”arden”, ”garden” are all suffixes of the string S.</li>
            </ul>
        </li>
    </ul>
    <p><strong>NOTE:</strong> A string of length <strong>‘N’</strong> has <strong>(N * (N + 1)) / 2</strong> substrings.
    </p>
    <p>&nbsp;</p>
    <h2><strong>Applications of strings</strong></h2>
    <ul>
        <li>String matching algorithms, which involve searching for a pattern in a given text have various applications
            in the real-world.</li>
        <li>String matching algorithms contribute to efficiently implementing Spell checkers, Spam filters, Intrusion
            detection systems, plagiarism detection, bioinformatics, digital forensics, etc.</li>
    </ul>
</div>