# Use case
<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Use case](#use-case)
    - [Extend](#extend)
    - [Include](#include)
    - [Different between Extend and Include](#different-between-extend-and-include)
    - [Example use case: Upload video](#example-use-case-upload-video)

<!-- markdown-toc end -->


## Extend

## Include

## Different between Extend and Include

## Example: Upload video

Actor: Member
Purpose: Upload video to the system
Description:
Type: Primary Use case
Pre-condition: **Member is logged in**. Member possess a video to upload
Post-condition: Video is uploaded to the system with all relevant information

Flow of events
| Actor Actions                                                      | Flow of events                                                                                       |
|:------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------:|
| 1. The use case behinfs when a member wants to upload a video      |                                                                                                      |
| 2. The member selects the video to be uploaded                     |                                                                                                      |
|                                                                    | 4. The system uploads the video and display the estimated waiting time                               |
|                                                                    | 5. The system prompts the user to provide necessary information such as video title, description etc |
| 3. The member enters the required information and confirms entries |                                                                                                      |
|                                                                    | 7. System verifies the information and prompts a successful message.                                 |
|                                                                    |                                                                                                      |

**Alternate flow**
4.a. Member uploads an unsupported video format and displays a message and prompts the member back to step 2 (NOTE: **not a failure scenario**)
4.b. Upload fails due to connectivity issues and member restarts the process from 1 step
7.c. The system prompts that information matches another video with the same name and asks to update it. 

**Exception flow**
4.c. The system crashes

NOTE:
1. **Don't make unnecessary assumptions ouster the scope of the domain.
2. Don't use terms like database, website, button etc unless explicitly mentioned
3. Always say that **use case begins with the something the actors wants**.
4. Try to go to present tense

