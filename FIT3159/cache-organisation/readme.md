# Cache organisation
<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Cache organisation](#cache-organisation)
    - [Practical skills related to cache organisation](#practical-skills-related-to-cache-organisation)
    - [Storage speed vs performance](#storage-speed-vs-performance)
    - [What is temporal and spatial locality?](#what-is-temporal-and-spatial-locality)
    - [Dirty bit for write back](#dirty-bit-for-write-back)

<!-- markdown-toc end -->

* Strongly impacts performance and functionality of all modern computers.
* Caches are critical to a system performance and a major area in contemporary machine design.


## Practical skills related to cache organisation
* Gives ability to optimise application code design to best take advantage of caches and thus *maximise application performance* - or avoid performance problems.
* Gives ability to anticipate likely application performance problems by relating application design to cache organisation in target platforms for the application.
* Gives ability to recognise and differentiate machine performance by understanding cache limitations - value for money when shopping for hardware.``


## Storage speed vs performance 

TODO what is storage hierarchy?

| Using fastest ram and cpu                                                   | Using DRAMs, SDRAMS, SSDs and rotating disks for storage |
|:---------------------------------------------------------------------------:|:--------------------------------------------------------:|
| This is the ideal if not costly                                             |                                                          |
| Speed: CPU can fetch instructions without incurring any significant delays. | Speed: Has lower performance due to TODO                 |
| Cost: Cost a lot                                                            | Cost: More economical                                    |
| High speed machines such as supercomputers use this method.                 |                                                          |


## What is temporal and spatial locality?
* Spatial locality specifies the probability of how close subsequent memory accesses are nearby to the current memory access.
* Temporal locality specifies the probability of how likely the access to the same area in memory will occur again a short time later.

* Fetches instructions are most frequent, follower by read operations of data then write operations of data.

## Dirty bit for write back


| Valid bit | Dirty bit |   |   |   |
|:---------:|:---------:|:-:|:-:|:-:|
| 1         | 1         |   |   |   |
|           |           |   |   |   |

If dirty bit is 0, no write back to memory. If cache is updated, dirty bit becomes 1, will write back to memory.
