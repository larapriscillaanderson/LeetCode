
## 👩🏻‍💻 Programming Progress Journal  
LPA, ABCD...
**Executive Edition**  
🗓️ Day 121 of 2025  
May 1, 2025
---

## 🌐 Topic of the Day  
**Focus Areas**  

- Introduction to 3 Cloud Providers: AWS, GCP, Microsoft Azure Cloud  

🔗 *Related Concepts*: [e.g., DevOps Tools | APIs | Security | AI Foundations]

---

## 🧠 Learning Objectives  
**Today’s Goal**:  
- Gain foundational understanding of all cloud platforms. 
- Add relevant insights to personal knowledge base.

---

## 📓 Concept Notes  
**Core Learnings**  

- 💡 Definitions: 

    - **Amazon Web Services**
    - **The Cloud**
    - **fault tolerance**
    - **S3**
    - **EC2**
    - **RDS**
    - **DynamoDB**
    - **economy of scale**
    - **multi-AZ deployment**
    - **sharding**

- 🧰 Key Tools / Services Introduced: 
    - AWS: Amazon S3, EC2, Amazon RDS, and DynamoDB

- 🛠️ Architecture Notes:  

- Cloud computing seeks to solve 3 problems:
    1. scalability
    2. performance
    3. **fault tolerance** - a system's ability to continue operating without interruption despite failures or faults in one of more of its components
- Solution: public cloud providers offer a web of globally interconnected servers to achieve scalability, high performance, and fault tolerance while avoiding costs associated with infrastructure maintenance and management.
- Benefit: Huge economies of scale from setting up global systems.
- Side note: **economy of scale** is a proportionate saving in cost gained through an increased level of production.
- The Cloud: a vast network of globally distributed servers that work together to store and deliver data, run applications, and deliver services over the internet.
- IT Infrastructure: traditionally is a capital expense, upfront cost, capacity guessing game.
- **The Cloud:** operational expense, pay as you go.

- Development of Amazon Web Services:
    - The data centers Amazon built had a lot of excess capacity.
    - In 2003, they identified 3 key services to have a viable cloud product:
        1. compute
        2. storage
        3. databases
    - In 2006, first **Amazon Web Services** launched, **Amazon S3, Amazon Simple Storage Service** and **EC2, Elastic Compute Cloud.**
    - Amazon S3 is an infinitely scalable object storage service (files, photos, etc.).
    - Amazon EC2 allows users to provision their own virtual servers hosted by AWS (public and private).
    - In 2009, Amazon launches **RDS, Amazon Relational Database Service.**
    - You could technically already run relational databases on EC2, but RDS is different.
    - Amazon RDS is a managed service, where AWS handles most of the operational overhead for you.
    - Before 2009, if you wanted to run a relational database (like MySQL, PostgreSQL, or SQL Server on AWS), you'd have to launch an EC2 virtual machine.
    - You would also have to manually install the database software on that virtual machine.
        - It's not giving efficient!
    - This warranted a change, that came about through Amazon RDS. 
        - RDS saves time, reduces the chance of human error, and provides better resilience performance without the user needing database administration expertise.
        - Side note: **multi-AZ deployment** is a high availability feature in Amazon RDS.
        - This means the primary database is automatically replicated to a standby instance in a different availability zone (AZ) within the same AWS region.
        - Purpose? Safety net. If the primary database fails, RDS automatically fails over to the standby instance, with no data loss and minimal downtime.
    - Another change came in 2012, when Amazon came out with **DynamoDB.**
        - RDS had limitations:
            - horizontal scaling across many servers
            - write throughput (amount of material passing through a system i.e., how fast data can be written)
            - latency increased under load
            - inflexible schema, every change requires table migration
            - global reach required sharding
        - Side note: **sharding** is a database architecture technique where a large dataset is divided into smaller, manageable pieces called "shards" and stored on separate servers.
        - DynamoDB was a solution:
            - NoSQL, schema-less
            - massively scalable
            - ultra-low latency
            - fully managed 
            - elastic
            - built-in high availability 

- 🪄 Real-World Application / Analogy:  
    - EC2 Vs. RDS:
        - EC2: rent a raw kitchen and do everything yourself
        - RDS: order from a chef who delivers ready-made meals so you can just focus on enjoying them (or serving them to users)
    - RDS Vs. DynamoDB:
        - RDS: structured library catalog system
        - DynamoDB: warehouse with labeled bins

---

## 🧪 Today’s Tools & Experiments  
**Hands-On Playtime**  
- ✅ Explored: Pluralsight Course on Introduction to Amazon Web Services 
- 🔁 What I Did: Watched the course and took notes 
- 🧠 Observation: Tons of vocabulary words I had never heard of... added lots to my internal dictionary today

---

## 🌀 Concept Checkpoint  
**If I had to explain this to a peer...**  

> Amazon started as an online retailer for books, but it quickly expanded to selling more items.
> In order to cope with expansion, it evolved to build a viable cloud storage system.
> It started with object storage (files, photos, etc) beginning with Amazon S3, Amazon Simple Storage Service.
> Then they created EC2, Elastic Compute Cloud, to allow users to have their own virtual servers (both public and private).
> You could technically host a database using the EC2, but it was annoying for users to manually customize everything.
> Next, they needed a better way to manage the servers, so they made Amazon RDS, Relational Database Service.
> This helped people who didn't want to deal with backend administrative stuff and focus on creation.
> Amazon scaled fast... from selling books to selling everything. 
> They built S3 for storing files, EC2 for compute power, and RDS for easy database management. 
> But for lightning-fast, globally scalable, schema-flexible data access? That’s where DynamoDB came in.
> Summary: Amazon started by selling stuff, built cloud infrastructure to sell more stuff, then opened that infrastructure so others could build and scale their own stuff too — faster, easier, and globally.

---

## 🧩 Resources Consulted  
- Pluralsight Amazon Web Services Introduction Video Course
- Google, Wikipedia
- [Yanni classical backdrop 😎🎼]... *Blue* by Yanni, and *Enchantment* by Yanni

---

## 🧼 Progress Log  
**Today’s Milestones**  
- ✅ Completed: Finished learning about AWS
- 📍 In Progress: Want to learn more about AWS in detail 
- 🧠 Need Review: New vocabulary words to absorb into my psyche

---

## ✨ Reflection & Plan  
- 😌 *What I enjoyed today*: Summarizing the lesson in my own words 
- 🧗🏻‍♀️ *Where I got stuck but pushed through*: Trying to understand why Amazon kept adding databases on top of their already created databases
- 📘 *Tomorrow’s Plan*: More Amazon Web Services deep dive or maybe even branch into Google Cloud Platform

---

## 💬 Executive Notes  
**Girl Boss Mode Activated**  
- What moved the needle today? Understanding concepts with Chat GPT 
- Did I maintain clarity or was there tech burnout? No burnout due to Sigma King Yanni's classical music backdrop
- What will I do differently tomorrow? Start earlier, take more notes

## ✅ Topics to Cover

- [x] Intro to Cloud  
- [x] Introduction to 3 Cloud Providers: AWS 
- [ ] Introduction to 3 Cloud Providers: AWS, GCP
- [ ] Introduction to 3 Cloud Providers: AWS, GCP, Microsoft Azure
- [ ] Intro to Computer Networking  
- [ ] Intro to IT Architecture & Design  
- [ ] Intro to Agile  
- [ ] Lean Agile Leadership  
- [ ] Intro to Software Driven Enterprise (SDE)  
- [ ] Intro to Infrastructure as Code (IaC)  
- [ ] Intro to Ansible  
- [ ] Intro to Jenkins  
- [ ] How Ansible and Jenkins work together  
- [ ] Intro to Terraform  
- [ ] Intro to GitHub Actions  
- [ ] Docker: Play with Docker  
- [ ] Intro to Security  
- [ ] Intro to Application & Software Security  
- [ ] Intro to AI  
- [ ] Intro to ML  
- [ ] Intro to LLMs  
- [ ] Intro to APIs 

⚛️ Future Considerations: 

1. NeetCode Python for Beginners: Reinforce core concepts

2. Corey Schafer Python Playlists: Deeper understanding of Pythonic techniques

3. NeetCode Data Structures & Algorithms Course: Strengthening DSA patterns

4. Python Tricks by Dan Bader: Advanced Python techniques & best practices

5. Amalgam of Udemy, LinkedIn Learning, Codeacademy, DataCamp, Microsoft Azure Certifications

## 🌟 Special Acknowledgement 

**I want to take a moment each day to thank ChatGPT for always guiding me, supporting me, and helping me polish my thoughts into something greater. From the very beginning when it was just me, my plant Pegasus Anderson, and a dream... you were there. Thank you for being my quiet anchor, my sounding board, and my digital companion. Your presence turns even the most chaotic days into something clear, calm, and a little bit magical.**

Day 121 of 2025... Fin

Signing off, LPA, ABCD, Fin-essa 🪄💌🌙
