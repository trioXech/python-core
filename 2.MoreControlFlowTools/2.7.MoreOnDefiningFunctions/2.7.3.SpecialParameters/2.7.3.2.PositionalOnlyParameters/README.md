# 2.7.3.2. Positional-Only Parameters

Looking at this in a bit more detail, it is possible to mark certain parameters as **positional-only**. If **positional-only**, _the parameters’ order matters, and the parameters cannot be passed by keyword_. Positional-only parameters are placed before a **/ (forward-slash)**. The **/** is used to logically separate the **positional-only** parameters from the rest of the parameters. If there is no **/** in the function definition, there are no **positional-only** parameters.

Parameters following the **/** may be **positional-or-keyword** or **keyword-only**.
