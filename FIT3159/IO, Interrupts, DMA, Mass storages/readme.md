# I/O, Interupts, DMA, Mass Storage and Hierarchies.
<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [I/O, Interupts, DMA, Mass Storage and Hierarchies.](#io-interupts-dma-mass-storage-and-hierarchies)
- [Why I/O, Interupts, DMA, Mass Storage and Hierarchies?](#why-io-interupts-dma-mass-storage-and-hierarchies)
    - [Asynchronous I/O](#asynchronous-io)
        - [Things I/O devices must do:](#things-io-devices-must-do)
    - [I/O devices](#io-devices)
    - [Polled I/O](#polled-io)
        - [Cons of Polled I/O](#cons-of-polled-io)
        - [How CPU Handling multiple devices](#how-cpu-handling-multiple-devices)
    - [Interrupts drive I/O and interrupts](#interrupts-drive-io-and-interrupts)
        - [Interrupt Process](#interrupt-process)
        - [Interrupt Timing](#interrupt-timing)
        - [How interrupts are detected](#how-interrupts-are-detected)
        - [Servicing interrupts using polling method](#servicing-interrupts-using-polling-method)
        - [Logic for handling interrupts](#logic-for-handling-interrupts)
            - [Normal operation](#normal-operation)
            - [Interrupt Operation](#interrupt-operation)

<!-- markdown-toc end -->


# Why I/O, Interupts, DMA, Mass Storage and Hierarchies?

* I/O, interrupts, DMA and mass storage's impacts the **performance and functionality** of all modern devices.

* Foundation knowledge: Mass storage is critical to **system performance** and a major area in contemporary machine design.

• Practical skills: Ability to configure a machine for good I/O
performance by making good decisions on interfaces.
• Practical skills: Ability to recognise and differentiate
peripheral performance by understanding specifications.
• Practical skills: Understand key concepts and problems in operating systems and device driver design.

## Asynchronous I/O
Computers are seldom operated in the manner where a program is started and the CPU is allowed to run it until it is completed. It sometimes must be **interrupted**.

CPU is allowed to run it until it is completed.
• The CPU must also **service I/O devices** 
• Such devices are designed to read, or read and write data, either to/from storage, a communications channel, or display device.


### Things I/O devices must do:
  * [ ] Must take a finite amount of time to complex a task.
  
  * [ ] Must be able to tell the CPU that is has completed an activity.
  
  * [ ] Communication adaptors and user input devices must be ready to accept input data destined for the CPU at any time. (The cpu must know a priori on exactly when this data will arrive)

The CPU must be able to service these devices without having to wait unnecessarily.    
    

## I/O devices 
* disks
* tapes
* keyboards
* mice
* graphics adaptors
* modems 
* CD drives 


## Polled I/O
The most simple strategy for servicing I/O devices is termed “polling”.

* In a polled system the CPU executes a program which **cycles through an endless loop**, checking **each I/O device once per loop to see if it needs to be serviced**, and then executing whatever main program it is to run.

* If a device needs to be serviced, the **CPU executes the service routine** and then resumes its **polling loop**.

### Cons of Polled I/O
* Response time: if a device becomes ready to be serviced just after it has been polled, it must **wait for the whole duration of the polling loop until it can be serviced**.

* Unpredictability of Response Time: since it is impossible to know a priori how many devices will need to be serviced, the **time to poll a device will vary with the number of devices ready to be serviced**.

### How CPU Handling multiple devices

1. CPU reads a status register in each device.
2. If the device needs to be serviced, service it.
3. One device is serviced, go to next device.
4. Once last device read/serviced, repeat.
   
## Interrupts drive I/O and interrupts
* Alternative to polling.

* Interrupt driven I/O are used in most **practical applications**

* Interrupting the CPU by providing a logical signal which says: "Immediately stop what you are working on and service me".

* Upon being interrupted by signal, CPU will cease to execute current program and jump to the start of the interrupting service routing (ISR) to service the **interrupting device**.

### Interrupt Process
1. CPU reads a status register in each device.
2. If the device needs to be serviced, service it.
3. Once device is serviced, go to next device UNSURE: that needs to be serviced

### Interrupt Timing
When the interrupting IO device interrupt signal (INT) is asserted, the CPU executes the Interrupting Service Subroutine ( ISR ) to service the device. Once the ISR is completed, it resumes executing the previous program.


### How interrupts are detected
In a microcoded CPU, at the beginning or the end of each instruction a **microword is used which tests the master interrupt line**.
* **Interrupt line** is **active**: the **next microprogram to be executed** is one which saves the state of the CPU, and then loads the PC with the address of the ISR.
* **Vectored system**: this microcode tells the device to assert its vector.
* **Hardwired CPU**: this function will be performed by dedicated logic.


### Servicing interrupts using polling method
 The central problem in handling interrupts is that of very quickly identifying which is the interrupting device.
• The simplest technique is to poll the devices which are wired to the interrupt signal.
• UNSURE: The first ready device which is polled is then serviced.
• Polled interrupt servicing slow, **many devices may need to be checked until the ready device is found**.


### Logic for handling interrupts

#### Normal operation
```psedocode
While running do begin:
    fetchinstruction();
    decodeinstruction();
    executeinstruction();
end
```

#### Interrupt Operation
```pseudocode
While running do begin:
    fetchinstruction();
    decodeinstruction();
    executeinstruction();
    
    if interrupts_enable and interupt_line_set then:
        begin
        .
        .
        end;
end
```


### Servicing interrupts via register
1. Any I/O device asserts INT.
2. CPU jumps to ISR.
3. ISR reads INT register, services devices as required.
4. Once ISR is completed, CPU resumes.


## Vectored Interrupts

* The most flexible technique for identifying an interrupting device is termed **interrupting vector**.
* In this arrangement, the interrupting device provides the CPU with the starting address of the ISR, so it can jump to the code required to service the interrupting device.
* Once the ISR has been executed, the CPU returns to executing the program which was interrupted

### Alternatives to vectored interrupts
* Interrupt vectoring can be implemented in a number of ways.
* The hardware to resolve priorities between interrupting devices can be embedded within the CPU or reside within an external device.
* Use priority resolution is when multiple devices may interrupt at the same time. Only one ISR can be executed at any time.
* The interrupt vector which is produced by the hardware can point directly at the starting address of the ISR, or it May memory. 
  

### Vector tables
* Where a vector table is used, each entry in the table is typically a **jump instruction** to the start of the ISR.
* The **first instruction** loaded into the IR is therefore a jump to the ISR proper, which then starts executing.

Pro: Each entry occupies the same space in memory, and that multiple vectors can point to the same ISR. The latter can save memory, where many I/O devices of one type are used.
Cons: The **ISR must execute an additional jump instruction when it starts**, and this can cost performance in a slower CPU.


## Example
100ns to poll
1000 ns to run ISR <- service time
25ns  <- reg decoding


10 devices

1. Polling - no devices to be serviced = 1000ns
           - 1 device to be serviced = 9*100 + 1000
           - no devices to be serviced = 0
           - 2 devices to be served = 2000ns + 25
