---
title: "Microsoft Intune Training | Complete Guide & Walkthrough"
url: https://www.youtube.com/watch?v=QaqQImyp3Ks
channel: Gregarious Technology
processed: 2026-07-26 10:59
subject_area: misc
series: false
tags: [microsoft-intune, mdm, mam, byod, compliance-policies, conditional-access, device-management, cloud-security]
chapters: []
source: destillo
---

# Microsoft Intune Training | Complete Guide & Walkthrough

**Channel**: Gregarious Technology | **Processed**: 2026-07-26 10:59
**Source**: [https://www.youtube.com/watch?v=QaqQImyp3Ks](https://www.youtube.com/watch?v=QaqQImyp3Ks)

## Summary

Microsoft Intune is a cloud-based endpoint management solution that centralizes management of devices, apps, and security policies. It serves as a single console for IT administrators to manage Windows, macOS, iOS, and Android devices, ensuring corporate data is protected regardless of device ownership. The video distinguishes Mobile Device Management (MDM), which controls the entire device, from Mobile Application Management (MAM), which focuses on securing data within apps, especially useful for BYOD scenarios. Compliance policies are introduced as sets of platform-specific rules that evaluate device health but require Conditional Access policies to actually block access to resources. Configuration profiles enforce settings like PIN policies, encryption, and network configurations.

## Key Points

- Microsoft Intune is a cloud-based solution for managing devices and apps securely from a single console.
- The core distinction is between Mobile Device Management (MDM), which manages the device itself, and Mobile Application Management (MAM), which protects corporate data within apps.
- Compliance policies assess device compliance with rules, but they do not by themselves block access; they must be paired with Conditional Access policies.
- Configuration profiles allow administrators to enforce settings like PIN requirements, encryption, and network configurations across enrolled devices.
- Intune supports company-owned and personally-owned (BYOD) devices, with MAM being especially important for BYOD to separate work and personal data.
- The demo shows that on enrolled Android devices, even in BYOD mode, administrators can perform actions like remote lock and send custom notifications via the Company Portal app.
- App deployment can be configured as 'available' or 'required', and administrators can monitor installation status directly in the console.
- Conditional Access leverages Microsoft Entra ID to control access to corporate resources based on device compliance and other conditions.
- A compliance policy by itself cannot block a device from accessing corporate data; it requires a conditional access policy to enforce that action.
- For BYOD Android devices, the work profile creates a separate container for corporate apps and data, ensuring personal data remains private.

## Notable Quotes

> MDM is all about managing the device itself while MAM focuses on securing the company data inside the apps.

> A compliance policy by itself cannot block a device from having access to corporate data.

> Think of it as your centralized control panel for Windows, Mac OS, iOS, and Android devices.


## Related Concepts

- Microsoft Entra ID conditional access deep dive
- Zero Trust security architecture with Intune
- Windows Autopilot and automated device enrollment
- Mobile Threat Defense (MTD) integration with Intune
- Intune vs. Configuration Manager (SCCM) for co-management

## Chapters

**0:00 - Intro** — The host introduces Microsoft Intune as a cloud-based endpoint management solution and previews the topics that will be covered in the guide, including key terminology, device enrollment, compliance policies, and a demo.

**1:25 - What is Intune** — Microsoft Intune is a cloud-based service that provides centralized management for devices and apps, helping IT administrators protect sensitive data and enforce compliance across various platforms. It integrates with other Microsoft services and supports both device management (MDM) and application management (MAM).

**3:50 - Key Terminology** — This chapter defines key Intune terms: MDM for managing entire devices, MAM for protecting data within apps, compliance policies that mark device compliance status, configuration profiles for device settings, and conditional access policies that enforce access control based on compliance.

**11:10 - Requirements & Licensing** — This chapter covers the licensing requirements for Microsoft Intune, including options for add-on licenses and selecting appropriate plans, as well as the necessary administrator roles (global admin, Intune admin, conditional access admin, etc.) and methods for assigning them via PIM or Entra. It also recaps the importance of having the correct subscriptions, assigning licenses to users, and following the least-privilege permissions model.

**17:35 - Intune Portal Tour: Dashboard** — This chapter shows how to customize the Intune dashboard by adding, moving, and deleting tiles, and then explores the Devices category, demonstrating how to view all devices and filter them by operating system like Windows.

**19:58 - Intune Portal Tour: Devices** — The chapter demonstrates how to navigate and manage devices in the Intune portal, including filtering by platform, searching by name, and exporting device data to CSV.

**22:39 - Intune Portal Tour: Enrollment** — The chapter provides a tour of the Intune Enrollment portal, covering settings for device platform restrictions, device limit restrictions, Windows Hello for Business, Autopilot, and corporate device identifiers.

**34:14 - Intune Portal Tour: Configuration Policies** — This chapter advises that security-related configuration policies should be created in endpoint security for better features, while other configuration policies are managed under devices and configuration. It also briefly mentions compliance policies, conditional access policies, and the use of sign-in logs.

**39:50 - Intune Portal Tour: Compliance Policies** — This section of the Intune portal tour explains how to use filtering options to troubleshoot conditional access policies by identifying where they succeed or fail.

**40:25 - Intune Portal Tour: Conditional Access Policies** — The chapter covers the platform scripts feature for running PowerShell scripts on Windows 10/11 devices, including testing and one-time execution, and introduces group policy analytics for importing and analyzing Active Directory group policies into Intune.

**44:19 - Intune Portal Tour: PowerShell Scripts** — The presenter discusses Windows update rings in Intune, explaining how to create multiple rings for test and production devices to manage updates, including a ring specifically for upgrading Windows 10 to Windows 11.

**46:22 - Intune Portal Tour: Group Policy Analytics** — This section demonstrates how to view the report for an Intune update ring to check statuses like success, conflicts, and errors, then explores the settings deployed within that policy.

**48:02 - Intune Portal Tour: Operating System Updates** — This chapter covers configuring Windows update ring settings in Microsoft Intune, including deferral periods for quality and feature updates, options for upgrading to Windows 11, handling pre-release builds, setting automatic update behavior, and enforcing deadlines with grace periods.

**1:15:34 - Intune Portal Tour: Device Cleanup Rules** — The chapter covers how to filter and view app deployment status in Intune, and introduces app configuration profiles and protection policies for managing app settings.

**1:20:06 - Intune Portal Tour: Apps** — This chapter explains MAM (Mobile Application Management) for controlling apps on BYOD devices and app selective wipe. It then covers Endpoint Security policies in Intune, including antivirus, disk encryption, and other security settings.

**1:29:14 - Intune Portal Tour: Endpoint Security** — This chapter tours the Intune Endpoint Security portal, covering BitLocker recovery keys, Windows firewall, EDR, and ASR policies. The speaker explains that recovery keys are stored in Azure, firewall is typically handled via group policy, and EDR requires a separate onboarding configuration.

**2:00:52 - Intune Portal Tour: Reports** — The chapter covers the tenant administration section of the Intune portal, including service health and message center, connectors and tokens for co-management and device enrollment, and customization of branding and support information for end-user experiences.

**2:06:52 - Intune Portal Tour: Users** — This chapter covers customizing the company portal branding and support information in the Intune portal, and emphasizes the importance of setting up terms and conditions for compliance and device enrollment. It also demonstrates how to create and manage terms and conditions policies.

**2:13:09 - Intune Portal Tour: Tenant Administration** — This chapter covers the fundamentals of device enrollment in Intune, including enrollment methods, the role of the Company Portal app, and the distinctions between corporate and BYOD enrollment.

**2:28:19 - Device Enrollment** — This chapter explains Intune enrollment restrictions, including managing corporate vs. personal devices, blocking legacy operating systems, and setting device platform and manufacturer limits. It also covers device limit restrictions to cap the number of devices a user can enroll, defaulting to five with a maximum of fifteen.

**3:16:48 - Compliance Policies: Fundamentals** — This chapter explains the process of creating device configuration policies in Microsoft Intune for Android Enterprise devices, emphasizing the differences between corporate-owned (fully managed, dedicated, corporate-owned work profile) and personally owned (BYOD) devices, and discusses how these policies can be supplemented with MAM policies to control corporate applications.

**3:21:49 - Compliance Policies: Create and Configure** — This chapter covers the creation and configuration of compliance policies in Microsoft Intune, detailing how to enforce device settings like passwords, security, and account restrictions while aligning with regulatory requirements such as HIPAA and NIST, and distinguishing between policies for corporate and BYOD devices.

**3:29:58 - Compliance Policies: Custom Antivirus Detection** — The presenter concludes the device restrictions configuration policy and moves to endpoint security, demonstrating the creation of a Microsoft Defender antivirus policy for Windows and describing its configuration options.

**3:36:16 - Configuration Policies: Device Restrictions** — This chapter covers configuring Windows Defender settings in Intune, including scheduling scans, setting threat actions, and creating separate antivirus exclusion policies for granular deployment to different device groups. It then transitions to discussing disk encryption policies like BitLocker.

**3:51:22 - Configuration Policies: Endpoint Security** — This chapter covers configuring BitLocker encryption policies for endpoint security, emphasizing storing recovery keys in Azure Active Directory/Intune, automating the encryption process, and recommending settings for preboot recovery messages and fixed drives.

**4:28:49 - MAM: Protection Policies** — This section covers configuring MAM protection policies, including setting minimum PIN length, enabling biometrics, enforcing app PINs even when device PINs exist, and defining conditional launch actions for failed attempts or offline access to protect corporate data.

**4:52:13 - MAM: Configuration Profiles** — This chapter explains the two types of Android apps in Intune: Managed Google Play apps (require enrollment) and Android store apps (suitable for MAM without enrollment), and demonstrates how to create and assign them.

**5:00:14 - App Deployment: iOS** — This section covers mobile app deployment for unenrolled BYOD devices, focusing on Android devices where users install corporate apps like Excel via the web company portal. It explains the process of finding apps, installing from the store, and handling authentication and management without enrollment.

**5:03:35 - App Deployment: Android** — This chapter covers deploying Win32 apps to Windows devices via Microsoft Intune, focusing on uploading the package file (created from an MSI) and configuring installation settings, while noting that the packaging process is detailed in a separate video.

**5:16:44 - App Deployment: Windows** — This chapter covers configuring detection rules for Windows app deployment in Intune, including MSI, EXE, file/folder, and registry key options, version checks, and handling dependencies and supersedence.

**5:36:18 - Common Mistakes & Best Practice** — This chapter covers common Intune management mistakes such as neglecting endpoint security policies, ignoring reporting, skipping pilots, mishandling BYOD vs. corporate devices, failing to plan for multi-platform support, and not keeping up with updates, along with best practices to avoid each pitfall.

**5:53:44 - Tips & Best Practice** — This chapter covers best practices for Intune, including regularly updating policies, using role-based access control with PIM, and integrating with Azure AD and Defender for unified security. It emphasizes that successful deployment requires careful planning, testing, and continuous improvement.

**6:11:44 - Demo: Windows** — This chapter covers key Windows device management tasks in Intune, including validating BitLocker recovery keys, reviewing managed app deployments and installation status, checking enrollment details, and accessing 'Access Work or School' settings on the device.

**0:00 - Demo: Android**


## Tags

`microsoft-intune` `mdm` `mam` `byod` `compliance-policies` `conditional-access` `device-management` `cloud-security`

## My Notes



## Distilled Report

[0:02] Hey everyone, welcome back to the Gregarious Technology channel. Today we're diving into Microsoft Intune, your all-in-one cloud-based solution for managing devices and apps securely. Whether you're an IT admin just getting started or whether you want to sharpen your skills, this is the beginner's guide that has everything you need.

[0:32] Here's what we'll be covering: What is Intune? Key terminology, requirements, and licensing. Intune portal tour, device enrollment, compliance policies, configuration profiles, app deployment, monitoring and reports, common mistakes, tips and best practices, and then ultimately a demo with a lot of these features. So we'll define these as we go along, get into the details and put some context to them. So let's jump right into it. So what is Intune? By definition, Microsoft Intune is a cloud-based endpoint management solution

[1:35] that lets you manage devices, apps, and security policies all from a single console. It helps IT administrators manage access to company resources and protect sensitive data. That's an important point — protect sensitive data across various devices including mobile phones, tablets, and laptops. So, think of it as your centralized control panel for Windows, Mac OS, iOS,

[2:07] and Android devices, no matter where your users are. Some of the main key benefits include features and components that facilitate things such as endpoint management, app management, and configuration of those apps, user and device security, compliance management. For example, if you're a government contractor or municipality and you

[2:39] have compliance regulations and some other industries as well such as HIPAA, NIST, DFARS, ITAR, CMMC, etc. You need to make sure that your devices are compliant according to these regulations of the industry. Continuing on with the key benefits — integration with other Microsoft services such as Entra ID, Microsoft

[3:10] 365 apps, simplified IT management, and support for zero trust security. Think about it: would you want to risk corporate data leakage such as contacts and proprietary data to users' personal iCloud and Google Drive storage? So, Microsoft Intune is an all-in-one cloud solution

[3:40] designed to address and manage all of these different aspects and much more. In order to understand the components of Microsoft Intune, we have to talk about some of the key terminology. So, let's break down a few key terms. Most importantly and generally speaking, MDM is all about managing the device

[4:12] itself while MAM focuses on securing the company data inside the apps, which is especially useful for BYOD — bring your own device setups — devices that the user may own but they want to access corporate data on. So the first key term is MDM — mobile device management.

[4:42] Intune's MDM capabilities allow organizations to manage and secure entire devices including company-owned and personal devices by enrolling them in Intune. This provides control over the device settings, security policies, app deployments, etc. And then there's MAM — mobile application management.

[5:12] Intune's MAM features focus on protecting the data within the specific apps, the corporate apps, regardless of whether the device is managed through MDM. This is particularly useful for BYOD — bring your own device — scenarios where employees use personal devices for work, accessing corporate company agency data. MAM is particularly useful for

[5:44] controlling the flow of data such as backups, copying and pasting between personal and corporate profiles on BYOD devices, etc. It's also capable of wiping corporate data only — wiping corporate data only — when a user is terminated or when a device is lost or stolen. It's essentially your gatekeeper to protect your corporate data.

[6:14] So in essence, MAM silos the corporate data into a separate profile than personal data on mobile devices. Compliance policies contain discrete sets of platform-specific rules. So you might have a compliance policy for iOS, for Android, and for Windows. And these rules and settings you deploy to groups of users and

[6:47] and/or devices. Devices evaluate the rules in the policy to report a device and its compliant status. It reports it either as compliant or non-compliant. So, a non-compliant status can result in one or more actions for non-compliance. By default, the only actions it can take on a

[7:19] device that's non-compliant without a conditional access policy is to mark it as non-compliant or to send an email that it is non-compliant. This is very important to understand: that a compliance policy by itself cannot block a device from having access to corporate data. So Microsoft conditional access policies

[7:49] can also use that status to block access to organizational resources from that device. So we tie the compliance status into conditional access policies as a requirement to say: if the device is non-compliant, then we're going to block access to it. That's typically how we do it. So it's important to understand that a compliance policy by itself doesn't take an action of blocking access to

[8:20] corporate data. You need to go into a conditional access policy, create a conditional access policy, and say that if the device is not compliant, they won't have access to corporate data. And next we have configuration profiles. Configuration profiles are used to manage and configure various settings on enrolled devices. These settings can include device restrictions which are probably most commonly used

[8:52] with configuration profiles. Things such as: they must have a PIN of a certain length — numeric, alphanumeric — PIN must be reset after a certain amount of time. The device has to be in a certain protection level with the device security, etc. So those security settings such as endpoint

[9:23] protection, network configuration such as VPN and wireless, and much more — those are all in the configuration profile settings that you can configure. They allow administrators to enforce policies and ensure devices are configured according to organizational standards. And then we have conditional access policies which we alluded to earlier. They control access to corporate

[9:54] resources such as Microsoft Office, Microsoft 365, based upon device compliance and other conditions, ensuring only trusted users, devices, and apps can access sensitive data, corporate data, company data. It leverages Microsoft Entra ID's conditional access capabilities.

[10:25] So you can actually get into conditional access through Intune or Entra. It's what that is alluding to. But they're both the same — it's the same behind the scenes. And Intune's device management and compliance policies enforce security policies. And that's what I was alluding to earlier — that conditional access really is the lock.

[10:55] And one of the conditions in conditional access policies is: if the device is not compliant, we can block access. That's the skeleton of Microsoft Intune and the core components. Of course, we would be amiss if we didn't talk about requirements and licensing for Microsoft Intune. You'll need a Microsoft 365 subscription

[11:26] that includes Intune — like Business Premium, or A3/A5 for education, or E3/E5 for enterprise licenses. Make sure that your users are either cloud users or synced from Active Directory with Azure Active Directory through Entra Connect if they're synced, and assigned appropriate licenses. Alternatively,

[11:57] you can purchase add-on licenses such as Plan 1 (P1) or Plan 2 (P2) as per your needs. So, let's say you didn't need everybody to have an E3 license. Maybe some of your employees are shop floor workers and they don't need Intune. Well, then you can possibly just have lower plans and then purchase the

[12:27] add-ons just for the users that need Intune. So, consider that as an option. I've included the link below which will give you the information on all of the compatible Intune licenses. So if we were to take a look at that link, you would see all of the compatible licenses listed here, all the different subscriptions.

[12:57] So you could take a look at that. To view your current list of subscriptions, you would go to admin.microsoft.com. You would go to Billing, expand that. Then you would go to

[13:31] Licenses. Click on that and you'll see your current licenses and subscriptions. Also make sure that the account you're logging into Azure has the correct admin role. Usually that's going to be either a

[14:02] global admin or the Intune administrator role. So if it's a global administrator role, obviously that has control over all of Office 365 and Azure for most of it anyways — that would cover all the necessary permissions for Intune and Entra and everything you have to do. And remember, there's some parts of Intune that require conditional access and creating

[14:32] groups and managing users and creating dynamic device groups and stuff like that that you might not have access to if you only have the Intune administrator role. So the Intune administrator role gives you full administrator role for Intune. But if you have only the Intune administrator role, then you might want to consider also having the role of conditional access administrator. Otherwise you might have to rely on others who have that role to configure

[15:03] the conditional access policies. User administrator role — and this is important again to create the groups that you need and manage users for the licensing, to assign, create and assign those groups for Intune. And then cloud device administrator. So there's pretty much two ways to assign these roles for Intune. You could either use

[15:34] privileged identity management — which is called PIM for short — to assign these roles, and PIM allows you to assign them for a discrete amount of time and allow authorization and acknowledgement and all that kind of stuff and expiration in a highly secure environment, or those roles can be assigned directly in Entra.

[16:04] So if we were going to assign those roles directly through Entra, we would go to portal.azure.com. We would go to Microsoft Entra ID. We would go to Roles and administrators. We would search for the role

[16:44] and select that role. Then we would click on Add assignments and just add the members to that role. And that's all there is to it. So as a recap: remember to have the right subscription and number of licenses available. Assign those licenses to the users that you want to have managed by Intune, and then make

[17:17] sure that the administrators in your organization have the correct role and only as much permissions as they need according to the RBAC least permissions model for what they need to do. Let's familiarize ourselves with the Intune portal. At this point, we'll just learn where to navigate to go in order to manage various

[17:49] features and components of Intune. We'll dive deeper into each topic in subsequent sections. So, open a browser and go to intune.microsoft.com to begin. On the left, you'll find sections for Devices, Apps, Users, Endpoint Security, Reports, and more.

[18:22] So, let's start with the Dashboard. The Dashboard serves as a central point for IT administrators to oversee device enrollment, application deployments, configuration settings, and monitor overall device health and compliance. The Dashboard provides a comprehensive view of the organization's endpoint environment, enabling proactive

[18:54] management and troubleshooting. It's basically a quick check on status and health for Intune. If you notice, there is an option to edit your Dashboard. If we click on that, we're able to move the tiles around as we please and add other tiles

[19:26] by selecting the categories and the resource types and then dragging those available to the tiles section. We can also delete by hovering over any individual tile and clicking on the delete button. And then when you're done, go ahead and

[19:57] click Save. Devices is one of the most important — one of the three most important — categories on the list on the left-hand side. Much of what we're going to be dealing with in this video is going to be underneath the Devices category.

[20:28] Notice that there are some quick buttons right here to manage your devices up top, but also on the left-hand side. If you go by platform, they're also on the left-hand side under By platform. So, we're currently underneath Overview, but if you go to Monitor and By platform, they're also on the left-hand side.

[21:00] If we go to All devices, we're going to find all of our devices in our organization for all platforms, with some summary information. You can add or remove columns, and you can also filter. So let's say I wanted to filter by operating system and I only want to see Windows devices.

[21:32] I could do that. And if we click on the device name, we're going to get all the information about that device. Now, we'll get into this during the demo section after we configure — well, we'll actually get into it when we do device compliance configuration and also the demo section. So, we're not going to go through these categories yet,

[22:02] but we'll just realize that you can get all the information for any device by clicking on the device itself. So, if we wanted to go back, we just simply click on Devices to get back to Devices. And we could clear the filter by exiting

[22:32] it out and get back to all of our devices. We can also search by name. So, if I knew the name of the device, we could search and get to that device easily. So, let's say we had thousands of devices and I just wanted to not filter — I wanted to just search for the device. That's how we do it.

[23:07] Of course, instead of filtering by operating system in All devices, we could go by platform and view the devices by platform. Notice we have an Export. So, we could export those devices to a CSV file and choose what kind of data we want in either All devices or By platform.

[23:41] So, next we'll take a look underneath Device onboarding at Enrollment and see what's in there. We will discuss in a subsequent section enrollment in more detail, but just taking a look at where things are at. Automatic enrollment — we take a look at what's in there. We've got the URLs for the automatic

[24:12] enrollment inside of there. CNAME validation — inside of there, what you're going to find is a section where you can test your domain name, your vanity domain name, and see if the DNS records for

[24:44] your CNAME records are created inside of your DNS registrar that are required for MDM. Co-management settings

## Raw Transcript

[0:02] Hey everyone, welcome back to the Gregarious Technology channel. Today we're diving into Microsoft Intoune, your all-in-one cloud-based solution for managing devices and apps securely. Whether you're an IT admin or just getting started or or or whether you want to sharpen your skills, this is the beginner's guide that has everything you need.

[0:32] Here's what we'll be covering. What is in tune? Key terminology, requirements, and licensing. [Music] Intoune portal tour, device enrollment, compliance policies, configuration profiles, app deployment, monitoring and reports,

[1:03] common mistakes, [Music] tips and best practices, and then ultimately a demo with a lot of these features. So we'll define these as we go along, get into the details and put some context to them. So let's jump right into it. So what is Intune? By definition, Microsoft Intoune is a cloud-based endpoint management solution

[1:35] that lets you manage devices, apps, and security policies all from a single console. It helps IT administrators manage access to company resources and protect sensitive data. That's an important point. Protect sensitive data across various devices including mobile phones, tablets, and laptops. So, think of it as your centralized control panel for Windows, Mac OS, iOS,

[2:07] and Android devices. no matter where your users are. Some of the main key benefits include features and components that facilitate things such as endpoint management, app management, and configuration of those apps, user and device security, compliance management. For example, if you're a government contractor or m municipality and you

[2:39] have compliance regulations and some other industries as well such as HIPPA, NIST, DEFARS, ITAR, CMMC, etc. Um, you need to make sure that your devices are compliant according to these regulations of the industry. Continuing on with the uh keep benefits uh integration with the other Microsoft services such as Entra ID, the Microsoft

[3:10] 365 apps, simplified IT management and support for zero trust security. Uh think about it. Would you want to risk corporate data leakage such as contacts and proprietary data to users personal iCloud and Google Drive storage? So, Microsoft Intoune is an all-in-one cloud solution

[3:40] designed to address and manage all of these uh all of these different aspects and much more. In order to understand the components of Microsoft Intent, we have to talk about some of the key terminology. So, let's break down a few key terms. Most importantly and generally speaking, MDM is all about managing the device

[4:12] itself while MAM focuses on uh securing the company data inside the apps. Uh which is especially useful for BYOD bring your own device setups uh devices that the user may own but they want to access corporate data on. So the first uh key term is MDM mobile device management.

[4:42] Intoune's MDM capabilities allow organizations to manage and secure entire devices including company-owned and personal devices by enrolling them in in tune. This provides control over the device settings, security policies, app deployments, etc. And then there's MAM, mobile application management.

[5:12] Intoune's MAM features focus on protecting the data within the specific apps, the corporate apps, regardless of whether the device is managed through MDM. This is particularly useful for BYOD, bring your own device scenarios where employees use personal devices for work uh accessing corporate company agency data. Ma'am is particularly useful for

[5:44] controlling the flow of data such as backups, copying and pasting between personal and corporate profiles on BYOD devices, etc. It's also capable of wiping corporate data only, wiping corporate data only when a user is terminated or when a device is lost or stolen. It's essentially your gatekeeper to your uh to protect your corporate data.

[6:14] So in essence, MAM silos the corporate data into a separate profile than personal data on mobile devices. Compliance policies contain discrete sets of platform specific rules. So you might have a compliance policy for iOS, for Android, and for Windows. And these rules and settings you deployed to groups or of users and

[6:47] devices and/or devices. Devices evaluate the rules in the policy to report a device and its compliant status. It reports it either is compliant or non-compliant. So, a non-compliant status can result in one or more actions for non-compliance. By default, the only actions it can uh take on a

[7:19] device that's non-compliance without a conditional access policy is to mark it as non-compliant or to send an email that is non-compliant. This is very important to understand that a compliance policy by itself cannot block uh a device from having access to corporate data. So Microsoft conditional access policies

[7:49] can also use that status to block access to organizational resources from that device. So we tie the compliance status into conditional access policies as a requirement to say if the device is non-compliant then we're going to block access to it. That's typically how we do it. So it's important to understand that a compliance policy by itself doesn't take an action of blocking access to

[8:20] corporate data. you need to go into a conditional access policy, create a conditional access policy and say that if the device is not compliant, they won't have access to corporate data. And next we have configuration profiles. Configuration profiles are used to manage and configure various settings on unenrolled devices. These settings can include device restrictions which are probably most commonly used

[8:52] with configuration profiles. Things such as they must have it pin of a certain length numeric alpha numeric you know pin must be reset after a certain amount of time. um you know the the device has to be in certain um protection level with the device security uh etc. So uh those security settings such as endpoint

[9:23] protection network configuration such as VPN and wireless and much more those are all in the configuration profile settings that you can configure. They allow administrators to enforce policies and ensure devices are configured according to organizational standards. And then we have conditional access policies which we alluded to earlier. Um they control access to corporate

[9:54] resources such as Microsoft Office uh Microsoft 365 based upon device compliance and other conditions ensuring only trusted users, devices and apps can access sensitive data, corporate data, company data. It leverages Microsoft Entra ID's conditional access capabilities.

[10:25] So you can actually get into conditional access through intoune or Entra. It's what that is alluding to. Um but they're both the same. They they it's it's the same behind the scenes. And Intune's device management and compliance policies to enforce security policies. And that's what I was alluding to earlier is that conditional access really is the um the lock.

[10:55] Um and one of the conditions in conditional access policies is if the device is not compliant, we can we can block access. That's the skeleton of Microsoft Intune and the core components. Of course, we would be a miss if we didn't talk about requirements and licensing for Microsoft Intoune. You'll need a Microsoft 365 subscription

[11:26] that includes in tune like the business premium or the A3 A5 for education or the E3 E5 for enterprise licenses. Make sure that your users are either cloud users or synced from Active Directory with Azure Active Directory through Entra Connect if they're synced and assigned appropriate license. Alternatively,

[11:57] you can purchase add-on licenses such as the plan one P1 or the plan 2 P2 as per your needs. So, let's say you didn't need everybody to have an E3 license. Maybe some of your your employees are uh uh shop for workers and they don't need intoune. Well, then you can possibly just have um lower plans and then purchase the

[12:27] add-ons just for the users that need in 10. Um so, consider that as an option. I've included the link below which will give you uh the information on all of the compatible intoune licenses. So if we were to take a look at that link, you would see all of the uh compatible licenses listed here, all the different subscriptions.

[12:57] So you could take a look at that. To view your current list of subscriptions, you would go to admin.microsoft.com. You would go to billing, expand that. Then you would go to

[13:31] licenses. Click on that and you you'll see your current licenses and subscriptions. Also make sure that the account you're logging into Azure has the correct admin role. Usually that's going to be either a

[14:02] global admin or the intoune uh administrator role. So if it's a global administrator role obviously that that has control over all of Office 365 and Azure for most of it anyways that would cover all the necessary permissions for intoune and intra and everything you have to do and remember um there's some parts of intune that require conditional access and creating

[14:32] groups and managing users and creating dynamic device groups and stuff like that that you might not have access to if you have only have the intoune administrator role. So the intoune administrator role gives you full administrator role for intoune. But if you have only the intoune administrator role then you might want to consider uh also having the role of conditional access administrator. Otherwise you might have to rely on others who have that role to configure

[15:03] the conditional access policies. user administrator role. And this is important again to create the groups that you need um and manage users for the licensing um to assign uh create and assign those groups for intoune um and then cloud device administrator. So there's pretty much two ways to assign these roles for in tune. You could either use

[15:34] privileged identity management which is called PAM for short to assign these roles and PAM allows you to assign them for uh a discrete amount of time and uh allow authorization and um acknowledgement and all that kind of stuff and expiration and highly secure environment or those roles can be assigned directly in Entra.

[16:04] So if we were going to assign those roles directly through Entra, we would go to portal.asure.com. We would go to Microsoft Entra ID. We would go to roles and administrators. We would search for the role

[16:44] and select that role. Then we would click on add assignments and just add the members to that role. And that's all there is to it. So as a recap, remember to have the right subscription and number of licenses available. assign those licenses to the users that you want to have managed by in tune and then make

[17:17] sure that the administrators in your organization have the correct role and only as much permissions as they needed according to the arbback lease permissions model for what they need to do. Let's familiarize ourselves with the intoune portal. At this point, we'll just learn where to navigate to go in order to manage various

[17:49] features and components of intoune. We'll dive deeper into each topic in uh subsequent sections. So, open a browser and go to intoune.microsoft.com to begin. On the left, you'll find sections for devices, apps, users, endpoint, security, reports, and more.

[18:22] So, let's start with the dashboard. The dashboard serves as a central point for IT administrators to oversee device enrollment, application deployments, configuration settings, and monitor overall the device health and compliance. The dashboard provides a comprehensive view of the organization's endpoint environment, enabling uh proactive

[18:54] management and troubleshooting. It's basically a quick check on status and health for in tune. If you notice, there is an option to edit your dashboard. If we click on that, we're able to move the tiles around as we please and add other tiles

[19:26] by selecting the categories and the resource types and then dragging those available to the tiles. section. We can also delete by hovering over any individual tile and clicking on the delete button. And then when you're done, go ahead and

[19:57] click save. devices is one of the most important one of the three most important um categories on the list on the left hand side. Much of what we're going to be dealing with in this video is going to be underneath the devices category.

[20:28] Notice that there are some quick buttons right here to manage your devices up top, but also on the left hand side. If you go by platform, they're also on the left hand side under by platform. So, we're currently underneath overview, but if you go to monitor and by platform, they're also on the lefth hand side.

[21:00] If we go to all devices, we're going to find all of our devices in our organization for all platforms. With some summary information, you can add or remove columns. And you can also filter. So let's say I wanted to filter by operating system. And I only want to see Windows devices.

[21:32] I could do that. And if we click on the device name, we're going to get all the information about that device. Now, we'll get into this um during the demo section after we configure well, we'll actually get into it when we do device compliance configuration and also the demo section. So, we're not going to go through these categories yet,

[22:02] but we'll just um we'll just realize that uh you can get all the information for any device by clicking on the device itself. So, if we wanted to go back, we just simply click on devices to get back to devices. And we could clear the filter by exiting

[22:32] it out and get back to all of our filters. We can also search uh by name. So, if I knew the name of the device, we could search and get to that device um easily. So, let's say we had thousands of devices and I just wanted to um not filter. I wanted to just search for the device. That's how we do it.

[23:07] Of course, instead of uh filtering by by operating system in all devices, we could go by platform and um view the devices by platform. Notice we have an export. So, we could export those devices to um a CSV file and choose what kind of data we want in either all devices or by platform.

[23:41] So, next we'll take a look underneath device onboarding at enrollment and see what's in there. We will discuss in a subsequent section uh enrollment in more details, but just taking a look at where things are at. Automatic enrollment. We take a look at what's in there. We've got the URLs for the automatic

[24:12] enrollment inside of there. CNAME validation. inside of there, what you're going to find is um a section where you can test your domain name, your vanity domain name, and see if the um DNS records for

[24:44] um your CNAME records are created inside of your DNS um registar that are required for MDM. co-management settings that deals with co-management between Intune and SECM which is now called MECM system

[25:15] center configuration manager um co-management between managing devices with active directory on premise SECM and Intune. Um, and I'll probably create a whole separate video on co- management in the future. Don't have one yet, but keep a lookout for that. You would have to uh basically create a profile um for the settings on that. Um, and this is where you'd find that

[25:55] Device platform restrictions are found here as well. And again, we'll be getting into this when we talk about enrollment, but that's where you're going to find uh the device restrictions by platform. Um, and these are basically uh what types of devices you want to be able to enroll and whether you want to allow corporate devices only or personal devices. So, if you click

[26:27] through the settings on this um you're going to find all those settings there. And there is the device limit restriction. So if we go in there and take a look, you can see um how many devices you allow for per each user to enroll in in tune. Now

[26:57] the maximum is 15. You can't assign any more than 15. So you can take this to any um you know anything up to 15. And then there's Windows Hello for Business. Now, this is the Azure only version of Windows Hello for Business if they're just Azure enrolled how you can configure this. It's very straightforward. Um, we're not going to

[27:29] get into this in this video, but this is where you'd find it. I will probably in the future again have videos on Windows Flow for business whether you're using Azure or hybrid but this is underneath enrollment if you're just doing the Azure uh joined only version of Windows Hello for business. Pretty straightforward.

[27:59] And then notice we have a whole section on autopilot. Autopilot is really for the out of the box experience when a user has a computer refresh or is getting a new computer. You know, how do we make that uh really efficient and automated and push all the apps and all that kind of stuff and configure the machine. Um, I do have a separate video that goes in

[28:30] depth into autopilot. So, if you're interested in that, take a look at the link I've provided below uh for uh the video on that. It's it's complex and it's beyond the scope of this video. Now, notice we were on the Windows tab up top. We're not going to go over Apple and Android because we'll go over those later in different sections, but I do

[29:00] want to point out a couple of other ones. The corporate device identifiers. If we click on that, what this allows us to do in the absence of using uh policies with Apple business manager and Samsung Knox administrator portal uh to import our devices as corporate devices, we can manually specify devices

[29:31] as corporate devices and that allows us much more control over the devices. So if we click on add we have a couple of choices. We can upload a CSV file and we can say okay what is the identifier serial number IMEI or the manufacturer model and serial

[30:03] number. And if we're going to stick with um the um serial number and hover over this, it's going to tell us how to format our CSV file. So, not not too much to get into this. It's pretty straightforward. You select how you want to do it. Um and then create the CSV file and uh select the file after it's been properly formatted.

[30:36] That's if you want to do it in bulk. If you want to do it manually one at a time, you can also do that. And it's pretty much the same thing. You're just instead of using a CSV, you're um manually inputting into the fields the data that's required. And again, it'll

[31:06] it'll give you some links on some more information on how to do that. And lastly, underneath enrollment, we have something called device enrollment managers. And let me hop over to the description of that. We take a look at that. What is a a device enrollment manager? A

[31:39] device enrollment manager DEM is a non-administrator user who can enroll devices in in tune. Device enrollment managers are useful when you need to enroll and prepare many devices for distribution. People signed into a DEM account can enroll and manage up to a thousand devices while standard nonadmin accounts can only enroll 15. So if you want some more information on that just

[32:10] look up uh device enrollment managers and there's a whole article on it. So if we wanted to specify an account that could enroll devices for users um so that the user wouldn't have to do it themsself then you would go in here to device enrollment manager and then add the user search for the user right here and then add them. So for instance I could do

[32:47] and then just add that user. Uh so uh important point that we just saw right here that user is not licensed with an in tune license. that user h has to actually have an intune license to be a a dem device enrollment manager. So very important to realize that.

[33:20] So our next category list, manage devices, is probably the most critical and important section underneath devices in the Microsoft Intune admin center. It's really the meat and potatoes of how do we configure and make our devices compliant to our

[33:51] needs for our organization. We've already defined uh these list items in our key terminology, but let's take a look at what they'd look like um from the portal perspective and what you're going to find underneath there. First off is configuration.

[34:21] So, if we click on that, we're going to see all of the configuration policies. Now, if people call them configuration profiles, that's understandable. I still call them configuration profiles because Microsoft, as you know, changes their terminology all the time. Initially they call them configuration profiles but now and they still do but now when you go to

[34:52] create they call them policies figures Microsoft anyways you're going to see all the existing policies profiles whatever you want to call them and the ability to create new policies. So, I do want to jump ahead just a

[35:23] little bit for an explanation because what happened was um the endpoint security is a relatively new component uh console in in tune. it didn't used to exist and it has newer features specific to endpoint security but on the back end it creates a configuration profile so anything I'm going to jump ahead here

[35:53] bear with me if we go to endpoint security and we create an let's say an anti virus or dis encryption or firewall call or EDR end uh endpoint detection or response or uh ASR attack surface reduction or account protection um or even conditional well conditional

[36:24] access is different. They're actually on the back end going to con uh configure a configuration profile or policy underneath configuration and vice versa. If you create a configuration profile that has to deal with security, it's going to show up underneath endpoint security. So my

[36:56] recommendation is is that if you're dealing with any kind of security profile that is in the endpoint security, create it in endpoint security because it's newer and has more features than the configuration profile itself. But either way, they'll show up in both. But for all other configuration profiles that don't have to deal with endpoint

[37:26] security, you're going to come to where we were. Again, I'm going to point it out is devices and configuration. and you're going to create a uh configuration policy /profile. So for instance, this ASR rules

[37:58] and the Bit Lacquer Windows and Microsoft Defender anti virus and Windows edr and Windows Labs. I did not create through the configuration um policies that we see here. I actually created those through endpoint security and they're still going to show up through

[38:29] um the configuration policies. I know it's confusing, but my again my advice is for any security stuff that shows up in endpoint security, configure those through endpoint security and not through the configuration profile. Everything else configure through the devices and configuration. That's not a security policy.

[39:00] Sounds clear as mod, right? But if you keep that in mind, um, go to the endpoint security for security stuff and any other kind of configuration stuff that you want to do. Go to devices and manage devices and configuration. Then you'll be okay. So, we're not actually going to take a look at these at this point because we have a subsequent um module

[39:32] on specifically configuration policies and we'll go through all the settings and see what settings are available. Um, but just realize that this is where you would configure this as it's we're going through the uh intoune portal uh tour. Next is compliance. This is where you create all of your

[40:02] compliance policies. You may have just the default. You may have to create separate compliance policies and assign them to um different groups or users. But again we are going to go into detail in a subsequent module on how to configure this. Next we have conditional access. Those are conditional access policies.

[40:37] So if we go here and then go to policies, we'll see all of our policies listed right here. And then we could always go and create a new conditional access policy.

[41:09] So again in uh a subsequent module we'll kind of overview this but I do have a couple of separate in-depth video uh videos on this because it is kind of complex. Um we'll we'll cover the basics in this video, but uh check out the links below for a you know a in-depth uh video on and and and more information how to uh fully configure conditional access policies.

[41:41] I do want to point out a very important feature that's very useful for um assessing um the conditional access policies, the sign-in logs. If you go to the sign-in logs, you can review the status of the conditional access policies with signins. So, notice a few things. It'll tell you the

[42:13] user. It'll tell you the status. And it'll tell you the application used to sign in through your conditional access policy. And if you scroll over, it will tell you whether it used multifactor authentication or not.

[42:48] Now, another important thing to point out about this is the add filters. You could filter by user.

[43:22] You could filter by many things such as conditional access or status. Status is a good one. You could click on status and say failure. I want to see the failures or

[43:52] interrupted. And in my case, there's no uh failures that are interrupted. So, a lot of options here, a lot of things to filter on. This is really intended to help you troubleshoot um if your conditional access policies are working, where they're failing, uh all that kind of stuff. So let's go back to devices

[44:22] underneath manage devices and take a look at scripts and remediation. This is a nice feature. So if we go to the tab for platform scripts, it allows us to add

[44:58] in this case a Windows 10 or later PowerShell script. And since we're not going to cover this in a separate section because it's pretty straightforward, um we'll just cover it now. You just got to locate the script that you the PowerShell script that you created as a PS1 file. And

[45:29] you want to run this as administrator. See, it's select no on this. I typically do not force a signature check um on scripts I write because it wouldn't work. And then say yes in uh 64bit PowerShell script host and then you would just next next all the way through this and assign it and it would work. So that's where you would do

[45:59] uh PowerShell scripts. It's pretty straightforward. You want to test your script first, make sure it works, and scripts will only run one time. They won't run uh, you know, consecutively over and over again. So, let's get out of this. And let's take a look at group policy

[46:29] analytics. In a nutshell, what this allows you to do is to export uh group policy objects from Active Directory and then you import them into Intune. you analyze them to to see how many of the settings are actually going to be working or allowed in in tune. So if we

[46:59] clicked here where it says MDM support, it would go through each setting of the group policy and tell us whether it's going to work or not. And then once we analyzed it, we can make a decision on whether we want to actually import it and we could actually

[47:29] import that group policy from active directory into intoune and save us a lot of time. So again, I do have a whole separate video because this is again uh a bit beyond the scope and and an an advanced topic. Uh so if you if you're interested in this feature, check out the link below. and we'll get out of this and go back to devices

[47:59] and manage devices. So now we're moving on to managing updates. If we look on the left hand side underneath manage updates, we can manage Windows updates, Apple updates, and Android fota firmware overthe-air deployments. Starting with Windows updates,

[48:34] we're going to see uh several different um components and options inside here. Up top at the first tab, the releases is just really uhformational, very basic stuff. We're um ju just getting information on um the Windows update releases and the deployment status and progress. And if we hit refresh, it'll tell us the progress. It'll tell

[49:04] us how many quality updates and feature updates are downloaded in the progress of those. Moving on to update rings. clicking on that. These are update rings for Windows 10 and later. Um, this policy is a collection of settings that configures when Windows devices that run Windows 10 or Windows 11

[49:34] updates get installed. You can create several update rings. For example, um you might create one for uh immediate delivery, no deferrals, and targeted to test devices um to make sure that the updates don't cause any issues. and then another with deferrals to production devices after you validated that the test devices, the

[50:06] updates that you've applied um actually don't cause any issues um and and run smoothly and get all the updates and all that kind of stuff. Another example of a separate update ring would be an update ring exclusively for upgrades of Windows 10 to Windows 11 and no other settings and targeting those Windows 10 devices only because upgrades from Windows 10 to

[50:38] Windows 11 is one of the options in an update ring. So if we take a look at the default update ring I've created for demonstration purposes and take a look at the settings in there, scrolling down. Uh well, actually before that, uh it's nice because you can uh

[51:09] view the report. You get a quick checklist right here about um you know the success conflicts, errors, all that kind of stuff. And you can click on view report. I'm actually not targeting any devices in this right now. Um it's just for demonstration purposes. So, you're not going to get anything in the report, but that's a um a very very useful section

[51:39] to be aware of to check and see the status of that that update ring. So now scrolling down, if we take a look at the settings, we'll see the settings right here that I've actually deployed in this policy. You get an idea of the different types

[52:11] of settings that you can uh deploy in an update ring. But I want I want to take a little deeper look at the options in some of these settings. So, because I've already created this, I'm going to go to edit. And by the way, we're going into a little bit more uh detail in the portal

[52:41] tour on this because it's pretty straightforward and we're not going to have a subsequent um module on this. Uh pretty straightforward. So, we'll just cover the update uh settings in the portal tour. They're pretty straightforward. So, obviously, we're going to want to allow Microsoft product updates. As far as the Windows driver updates, that's up to you. Allow block.

[53:11] You could have a separate update ring for driver updates and uh target different devices for that and have deferral um different deferrals and or or just test it to a target group and then decide whether you want to push that out to production or not. Uh that's totally uh you know configurable and up to you. This example is more like a

[53:42] production deployment of an update ring. So for quality updates, I defer them for 7 days in case there's an issue then I can remediate that. Same thing with feature updates. And the idea is that I'd have another update ring that would deploy to test devices before this update ring kicks in. You can make it 15, 30 days. Wouldn't make it much

[54:12] longer than probably 15 though. Here's the option to upgrade Windows 10 to Windows 11. I suggest maybe creating a separate update ring just for that and targeting only the Windows 10 devices and basically not configuring much else in here having a separate ring for that. You can set the

[54:44] update uninstall period as we have 10 days in my example to uninstall those uh feature updates. In my example, I have not configured uh pre-release builds. However, if you choose to enable that, you're going to have this um option box list on whether you want um the release

[55:18] preview, the beta channel, or the dev channel. And again, if you choose this as an option, this might be a separate update ring targeted to test computers only. I wouldn't do this in a on on all production computers right off the bat, especially with pre-release builds. So, this is a prime example of when you would have a separate update ring just for pre-release builds to test set.

[55:52] So we'll leave that at not configured. You have several options for automatic update behavior. I chose auto install at maintenance time which gives us the options for specifying active hours start and active hours end.

[56:23] So that the maintenance time would be outside of those hours. Those are your working hours. So if you choose auto install at maintenance time, it would be outside of the active hours. You also have just notified download, autoinstall, and restart. at maintenance time.

[56:54] Um, auto install and restart at scheduled time, auto instart, auto install and reboot without end user control or reset to default. And you can have different options depending on what you choose for your update behavior. I've set my policy to disable the end users from pausing Windows updates.

[57:24] Of course, you could enable that, but I don't like that. I do like the idea that users can check for Windows updates at any point. The change notification in this policy, I said set it to the default update notifications, but you do have several options in

[57:54] there. Um, turn off all notifications and excluding uh restart. So, they'd only get a restart warning uh once all the updates have been downloaded and installed. And you also have the option to turn off all notifications including restart warnings and they won't receive any notifications as the end user.

[58:24] I do like to set deadline settings so that I can enforce if the user keeps pausing or whatever the updates ultimately the the security updates essentially or most importantly need to be applied. So, I like to say aloud. And so, for feature updates, just as an example, um I've said 15 15 days,

[58:54] deadline for quality updates, seven and a grace period of one day. After these deadlines have expired, they have a grace period of one day. Otherwise, it's going to autoreboot which is shown right here. And those are all the available settings for the update rings.

[59:27] So, if we go back to Windows updates at the top tab, let's take a look at feature updates now. So, the feature updates for Windows 10 and later. Uh, this policy updates devices to the Windows version. for example, 24H2 for Windows 11 that you

[59:59] specify and then freezes that feature set version on those devices. So, you could set several uh feature updates as they come out. And um if you do that, then the devices that you target are going to stay on that feature update until you do a new feature update policy. and of course target devices with a device group or user group or whatever.

[1:00:29] So, taking a look at my example right here, the default features uh feature updates which I've already created. And if I go to view my deployment settings, we can see which options are available. very very limited. But um basically you're just defining

[1:01:01] which feature update you want to update them to and as new feature updates become available then there will be new feature updates in the list. So the only real selection here that's important is right here, feature update to deploy. And then of course um initially you might want to just do this to a test group of devices

[1:01:31] and then when all is tested and validated just fine then you can move it on to production. Um so again you could have uh multiple uh feature updates and deploy them to different target groups. So doing that if we take a look at at our current selections here we have um up to the latest version of Windows 11 and of course Windows 10 the latest version as well. But as we know,

[1:02:01] Windows 10 is either out of support at this point or going out of support. So as um new feature updates become available in Microsoft, this list will update. So, let's go back and take a look at the top tabs again

[1:02:32] and take a look at quality updates. What are those? Okay. So, quality updates um expedite the install of the most recent Windows 10 and Windows 11 security updates without the need to pause or edit existing monthly servicing policies. So, this these are expedited um updates um outside of your normal

[1:03:03] policies. Now notice if you see up top here I'm getting a warning that says creating quality update policies requires specific licensing learn more about prerequisites and quality update policies. I don't have an appropriate license. If I want to go ahead and try to create quality update policy or an expedite policy, I'm not able to do that. So, you

[1:03:35] could click on this and see what the prerequisites are. Probably at least in E3 and E5 um uh which I I I currently don't have, but you can check that out. And just pointing out right here, it tells us that Windows 10 is reaching end of support on October 14th,

[1:04:05] 2025 to stay protected. Upgrade to Windows 11 or purchase extended security updates ESU. Now remember in our uh update rings we can actually actually create a ring to upgrade Windows 10 to Windows 11 and do this through intoune totally automated. Pretty cool feature. But of course I'm going to sound a

[1:04:35] little bit like a broken record. Never ever just do update rings to production. all production computers. Right off the bat, any update ring you create, I would first create one for uh testing, piloting to a security group that includes only test computers, and that's the target assignment. And then test it out

[1:05:06] for I don't know, a good week or two, maybe even a month. and try to blow it up, see if there's any issues, and then target production computers with an assignment after that. So, let's move on to Apple updates. At the top, let's start with the tab for

[1:05:38] iOS iPad OS update policies. I haven't actually created any in my my own tenant either for demonstration or for production. So, let's they're they're pretty straightforward, but let's just go through the motions here to see what the options are.

[1:06:08] >> Okay. So, For iOS and iPad OS, there's really only two options. The version to install and the scheduled type. That's it. That's all you really need, though. Now, you could have several different um iOS policies and target different devices

[1:06:39] and different device groups. It depends on your organization and your needs. Taking a look at the version to install. Again, this list is going to be updated as the iOS updates come, you know, come into play and get updated, but you can choose the version um that you want to update these devices with. Again, you

[1:07:09] might want to have a test pilot uh device group and have one iOS uh policy that you test out with test devices and then bring another policy when when you validate that and fully test it, you can bring that policy into production or have a separate policy for produ production that you don't assign until later. And then you also have

[1:07:40] the schedule type. And taking a look at that, the options are update it next check in update wi which is not going to have any options. If you if you leave it at that, it's just going to say next time it checks in, update it. That's it. No options. But if you say um update during scheduled time, then you're going to have your time zone,

[1:08:11] you're going to have you can select your time zone and then you're going to have your time window. So this is basically your maintenance window when you know what uh what which time zone I am I in according to UTC. Um and then according to that UTC time zone, when is my maintenance window

[1:08:44] start? Well, I mean the start day and the start time, end day and end time. And it's pretty much the same thing with uh outside of time, scheduled time. So, it just depends on how you configure this. Okay, let's go back to Apple updates.

[1:09:14] Let's go back up to the top and this time we're going to choose the tab for the MacOSS update policies. Now, you're going to have quite a few more settings in these uh well, they call them profiles, but really they're policies. Um because obviously a full-blown operating system like Mac OS has a lot more options than a you know a mobile device operating system as far as

[1:09:45] updates and all that kind of stuff and control. So if we create a profile and take a look at the available options and settings first taking a look at the critical updates options we have download and install. download only, install immediately,

[1:10:18] notify only, or install later. So, let's say we choose download and install. Well, that's what it's going to do. Notify only. That's what it's going to do. Um, pretty much self-explanatory. Again, you might want to have separate um update um profiles for this and target different devices all depending

[1:10:48] on your needs. But always test your pilot first to make sure there's no adverse effects and you validated all the settings. Next, we have firmware updates and pretty much all the same options. And same thing with the configuration file updates.

[1:11:19] Pretty much all the same options and again with all other updates pretty much all the same options. We do have the schedule type

[1:11:49] and clicking on those settings, those options. Update it next checkin is not going to have any options. We would have to do the same thing we would do with an iOS or iPad OS operating system if we wanted to schedule it. We'd have to choose this, choose our time zone, and choose our time window, just like we did with iOS

[1:12:20] and iPad OS. And that's pretty much all there is to the ample updates for the MacOSS. So, let's go back to Apple updates. And then there's just a monitor tab, but I'm not actually um deploying any of this, but you could check on the status of of of all the Apple updates.

[1:12:51] And lastly, we have Android FOTA, firmware overtheair. So, it's important to realize that first of all, you need a connector for this to work. And it has to be a corporate device identified as a corporate device with a corporate um

[1:13:22] enterprise management solution. So for instance, Samsung Knox admin portal that you enrolled your devices in that manages them as corporate devices. Also notice that to use this add-on um you'll have to have a trial or buy licenses for this.

[1:13:56] If we click on learn more, we will get some information on how this works. You can use Microsoft Intoune to manage software updates on the following Android enterprise devices. Fully managed, dedicated, and corporateowned work profile devices. These are not BYOD devices.

[1:14:28] You have to have some sort of uh enterprise management solution for this to work. And so it'll bring you to the article on how to configure all this stuff. Um quite a bit to configure. We're not going to get into all that, but just know that it's it's an option and you could read through this article to um understand what's involved.

[1:14:59] And one last thing, you have to set up the connector which is right here. So if you clicked on that it would bring you to the space where you can set up the connector. Um but uh obviously you have to have all the prerequisites in management uh enterprise management solutions in place and the requirements to be able to do that.

[1:15:37] So now we will move on to device cleanup rules. And if we click on that, notice at the top there's a description on what these device cleanup rules do. Cleanup rules. Remove intoune enrolled devices that are

[1:16:10] inactive or unresponsive. These rules are applied every 24 hours. Once a device checks in again, it will still be enrolled without further actions from you. So basically, it's a cleanup. If uh devices have been removed from your organization and you forgot to remove them from intoune or if the device is lost or stolen and the user cannot uh

[1:16:42] authenticate to remove it from uh intoune enrollment as a security measure. However, let's consider the case that uh a user is on sbatical or a leave of absence and then they return. Well, as soon as they log back in, uh the user would uh authenticate and then the device would become um active and reenrolled without any further action needed on your part.

[1:17:14] So, if we take a look at a um rule that I've got in place right now and take a look at uh what I've got configured in that rule. it um basically says the platform is Android personallyowned

[1:17:47] work profile. This is BYOD devices that they have a work profile on for work um work uh corporate data and it says if they haven't checked in in 30 days then um clean up that device from enrollment. And when we clean it up from enrollment it basically no longer becomes a managed device.

[1:18:17] And thus, if you have your conditional access policy set up correctly, if it's not enrolled and doesn't uh fit the rules of the condition conditions of the conditional access policy, then that device would not be able to gain access to corporate data. Unless, of course, that device comes back online, the user authenticates, and it reenrolls.

[1:18:47] So, if we go back to device cleanup rules and create, we will see that we can create a rule for device cleanup for any of the device operating systems that can enroll into

[1:19:21] and uh Android device administrator is legacy. This is the current one. Um, iOS, iPad OS, Mac OS, Windows, holographic, holographic, um, tvOS, all those operating systems. And that is pretty much all there is to explain about that

[1:19:52] other than you just specify the operating system in older than x number of days uh to have it um clean up out of enrollment. That's all there is to the policy. So now we're moving out of the parent category on the left menu of devices to apps. Let's click on that.

[1:20:23] So I want to point out that we have two main sub menus underneath apps platforms and manage apps. We also have all apps. So from all apps or platforms, that's really where you're going to deploy apps for any operating system. So, if you go to all apps,

[1:20:58] we'll see that we can create an app for pretty much any type of operating system that uh Intoune can deploy apps to. But if we want to just kind of narrow it down and and of course you're going to see all apps that are deployed underneath all apps. You can create apps from all apps.

[1:21:30] But if we want to go to the uh predefined filters for the operating systems for each one of those, it just gives us a more narrowed filtered view. for both viewing those apps by platform and creating apps by platform. Notice in all apps that we have some

[1:22:01] filters uh will help us sort through the information. We can sort by assigned to see the assigned. So if we went to assigned, we could see assigned apps only or unassigned apps. Helps us filter. Oh wait, we didn't assign this app yet or we was assigned this this app. We could also filter by platform and date added. data added is

[1:22:32] kind of nice because then we can see how old these assignments are and if the apps need to be updated or the most recent ones. So we can see um on the ones we just recently deployed. If we click on any single app that we have created, we can get a status on the deployment. So this one

[1:23:04] has been superseded by another app. We haven't deployed it. So we're not getting much information from this. Moving back, we'll take a look at this version of sevenzip that superseded it. It's a newer version. And take a look at that deployment.

[1:23:41] And again, there's nothing in inside of here. Let's take a look at uh Microsoft Word for Android. Take a look at the status on that. And you can see says two installed, zero not installed, zero failed, zero pending, zero not applicable. Then you could actually click on the status and get some more

[1:24:13] information on the devices or users that it was installed to. And it's pretty much the same thing. If you filter underneath platforms, you'll get the same information. Um, same type of filters just minus the

[1:24:43] operating system type. You'll still be able to create. We'll go through this um when we go through the subsequent module on creating apps. So, we're not going to go through this right now. But it's just a way to isolate by operating system on the apps to view which apps have been deployed and their

[1:25:13] status and to deploy uh new apps no matter whether you go to all apps or by platform. So underneath manage apps we have configuration and a configuration is called a configuration profile for your applications and it allows you to uh configure apps that you have um already deployed to

[1:25:44] configure certain settings on those apps. So for instance, I configured something called smart switch. And what it really does is it, if we take a look at that, it configures the settings for that application and pushes it out, assigns it, and then pushes it out after assignment to whatever group or you know users or group uh or or devices

[1:26:16] in those groups or group or groups with that configuration. So, so if you wanted to configure an app after you push it, uh you would go to app configuration and you would configure the uh settings for that application and assign it and those configurations would be pushed out to that app for that group assignment. Again, we'll get into some more detail when we go through apps in a subsequent

[1:26:47] module. And then we have protection. These are app protection policies also known as ma'am microsoft application management. And yes, we'll get into more detail in the apps module about this, but this is

[1:27:18] controlling apps at the app level, not at the device level. This comes in particularly handy with BYOD devices where you cannot control the device itself but you want to control the flow of company data as we defined earlier in our terminology between your corporate data and your personal data.

[1:27:49] So this is where you configure ma'am and ma'am can come in two flavors. You can use ma'am with enrolled devices or without enrollment where uh BYOD devices um are not managed and you're simply controlling the apps themselves. And the company portal app does not

[1:28:20] actually enroll the device. It just manages the apps. Taking a look at app selective wipe. That allows us to either create a wipe request for all company data for a user or and what we just looked at was underneath WIPE requests.

[1:28:52] for app selective wipe. Or we can go to user level wipe and do a user level wipe per user instead of per device. So now we're moving on to the parent category of endpoint security in the

[1:29:22] main list and in tune on the left hand side. Endpoint security provides a central location for managing various security policies and settings across your managed devices. It allows you to configure and deploy security settings for anti virus, firewall, disk encryption,

[1:29:52] attack surface reduction, account protection, and more. When you create policies here, they will show up underneath configuration policies because on the back end um they're just configuration policies. But this is the front end, the new way to create um the security policies uh that are specifically configuration policies as security policies.

[1:30:24] I highly recommend that you create these policies here instead of um using an endpoint protection configuration profile template. Um when we get to configuration profiles, you'll see what I'm talking about. It allows you when you do it in this method in this fashion to focus on each separate security component. It includes each of these components include

[1:30:54] additional security components and updated features and settings that you're you might not find specifically in the configuration policies um separately. It allows you to focus on each separate security component and includes additional security components and updated features and settings.

[1:31:24] First, we have the anti virus endpoint protection endpoint security settings. And you're going to find a status of the end points um that this is delivered to up top. And you can click on that and get some more details and information on

[1:31:55] also um active mailware if there's any active malware found. But specifically, we're talking about creating a policy for an anti virus policy. And if you see here, I've already got one configured.

[1:32:27] So, if we click on that and we go down to the configuration settings that I've already deployed and edit those, we we can see what kind of uh settings are available in an anti virus endpoint security policy. We're talking about archive scanning,

[1:32:59] behavior monitoring, cloud protection, removable drive scanning, network drive scanning, um things such as UI access, user interface access, um block levels, uh full scans, excluded processes, PUA protection, Um when to uh update the signatures, actions on uh certain levels of threats,

[1:33:35] um schedules, all that kind of stuff. All that kind of stuff is included in your um Microsoft Defender Antivirus scary settings. It's important to point out this is just for Microsoft Defender antiirus. It does not manage any third-party antiirus uh solutions that you have. That's a whole separate topic. So,

[1:34:06] let's go back and take a look at disk encryption. Most commonly I deal with Windows encryption which is Bit Locker. But there is the possibility of creating uh disk encryption policies for

[1:34:36] Mac OS as well. So um just keep that in mind. If we take a look at the settings that are available in Bit Locker and the policy that I have, first of all, notice the status and user checkin up top.

[1:35:07] You can click on view report to get more details. on each one of these that have receive the policy from the targeted group and all the individual settings in the policy that have actually succeeded or failed and click on those to get more

[1:35:37] information. If there were a failure, you could check on the failure. Now, you can do this from the device end as well because that's all we're really doing when we dig down this bar as we're looking at the device end. But if we go back into the policy and take a look at the available configuration settings

[1:36:08] from the policy that I've created, see all available settings. You'll see categories and underneath each category there are various selections for uh general Bit Locker settings as well

[1:36:38] as each type of drive whether it's an operating system drive or a fixed data drive or movable drive. Now, I do have a whole separate video on this. I'm going to include the link below. So, check that out. One of the nice features of using Intoune is that it will save the recovery key information to Azure and Intune so that you can recover

[1:37:09] it, which is uh a heck of a lot easier than trying to use AD or manually record those. they're always recorded in Azure. So if that a device let's say we replace a hard drive and um all of a sudden it recognizes new hardware and you can't or you know or a motherboard or whatever video card whatever and it triggers a a bit locker recovery some sort of hardware or there's a corruption of the

[1:37:40] hard drive or something anything that could recover or or I'm sorry trigger a recovery in Bit Locker and it's not booting It's asking for the recovery key. Um, using this method and making sure that we do the right selections, um, that recovery key for that device will be stored in Azure and we'll have no problem recovering that recovery key, uh, locating and copying that recovery key.

[1:38:11] So for instance, if we went to that device inside of Intin went to recovery keys and then show recovery key, it'll actually show us the recovery key ID and the actual recovery key. we can show it and then we can actually copy it and then we could paste it and give it to the end user or you know

[1:38:45] just read it out loud to the end user whatever. So again for full uh a full in-depth video on this uh go to the link I pasted and check out that video. Next is Windows firewall. I'll be honest, I almost never configure this for any customers.

[1:39:16] Uh typically this is handled either through group policy with a simple group policy object that says uh linked to the default domain that says turn off Windows firewall for all computers or to uh computers OUS um and not the servers OUS or the main controllers OUS to turn off the Windows firewall because typically the firewall protection is at the router level not the Windows level almost no

[1:39:46] organizations use this but just be aware that you can create policies um for fire Windows firewall and if we did that again we've got Mac OS Windows for configuration manager if you're in co- management mode but typically be Windows

[1:40:16] And then we could do the firewall or the firewall rules. Um firewall would just cover the general firewall settings and the firewall rules is where you could implement specific rules. And that's just about all I'm going to say about this. And we have EDR, endpoint detection and response.

[1:40:50] So going in there and scrolling down, just like many other Intune control panels, you've got a status up here. Windows Defender for Endpoint. We'll talk a little bit more about the integration with Windows Defender for Endpoint in a minute. But here we can see that one device is

[1:41:20] onboarded and one device is not onboarded to Windows Defender for Endpoint which is not in TIM. We can create a policy and we can create a policy for Windows, Linux, Mac OS or Windows in co- management mode with configuration manager SECM MECM.

[1:41:54] So taking a look at the policy that I've already created again a summary panel for device and user check-ins status and you can click on report view report for more information. Scrolling down to take a look at the settings that I've already configured and available settings underneath configuration settings.

[1:42:29] There's really nothing in here other than how you onboard and how you share information with Microsoft. So taking a look at the description for the defender for endpoint client configuration package type. It provides a description of EDR. Microsoft Defender for Endpoint

[1:42:59] Endpoint Detection and Response EDR capabilities provide advanced attack detections that are near real time and actionable. Security analysts can provide alerts effectively, gain visibility into the full scope of a breach and take response actions to remediate threats. That's what EDR is.

[1:43:30] Notice that my current uh configuration package type is onboard and once you set that you cannot change it. But if we go back and start a new policy

[1:44:01] for Windows for EDR. We can see the different options on board and offboard. It's very straightforward with very little options to configure. I would recommend if you don't if you're not familiar with EDR

[1:44:32] um do some research on it, but definitely want to deploy this as a security measure. Next is ASR attack surface reduction. We can create a new policy.

[1:45:02] Our only options are Windows or Windows Config Manager, which is SECM, MECM, System Center Configuration Manager, if you guys aren't familiar with that yet. We'll take a look at my current ASR rules policy to see what I've configured and what's available.

[1:45:33] We do have the device user and check-in status and view report up top, which is pretty typical. Scrolling down, we can take a look at what I've configured and what's available through the configuration settings. So, you get a pretty good idea of what

[1:46:03] ASR is all about through the available settings in here. um blocking scripts, macros, executable files, office communication, um a lot of stuff with Office and in Adobe Reader with creating child processes in subprocesses, JavaScript, um

[1:46:33] shell creation, uh assigned processes, uh, driver exploitation, um, more stuff on Office with executables and all that kind of stuff, ransomware, executable content, and email and

[1:47:03] webmail control. controlled folder access and all sorts of exceptions. Um, so again, I would recommend that if you want some more information on ASR and you know what it's all about, do your research. Um, but some of these are pretty self-explanatory. You can

[1:47:34] always click on each one of these information icons and get more information on those. And you can always click on learn more. It'll bring you to some more settings and information about those. But it's really dependent on your environment, what you need to envir uh run in your environment um as uh absolutely necessary for production. My recommendation is if it's not necessary for production and you

[1:48:07] um can block it as a risk, then go ahead and do that. And uh you can always go back in and change that setting. And it as always, you never roll this out to production to begin with. You always start with a test or pilot group and see how it runs with all the applications. and um needs of the organization, see if we run into any issues and make uh make um accommodations and changes and then

[1:48:37] adjust and then try again. So let's go back to endpoint security and now account protection. So in account protection when we go to create a policy we have several options different types of policies for Windows anyways

[1:49:09] we can do an account protection policy a local admin password solution lapse or local group membership. Um, account protection and group membership are pretty self-explanatory. Most often what I see is a requirement or request to configure the local admin password solution lapse in in tune through the account

[1:49:41] protection in the endpoint security admin control panel. And so that's what I've configured and we'll take a look at that. So opening up my configuration that I have for laps already. Again, we see an overview of the device and user check-in status and you can uh

[1:50:13] view the report. Scrolling down to take a look at the settings that are available and what I've configured in laps. It's all about that local administrator account and uh how you want to set that up. So you're going to have a backup directory

[1:50:44] for uh if we take a look here says use this setting to configure which directory the local admin account password is backed up to and you know several options. So we can back up that local admin account password to disabled. Password will not be backed up which is a default. Then same thing that's not configured. Back up the password to Azure AD only or active directory only.

[1:51:15] And here's where you can rename that local admin account which is highly recommended. You want to not use the default administrator name because that's a security risk. Everybody knows that the default name for Windows local admin login is administrator. And if

[1:51:46] that account is enabled, well then they might be able to do a password spray attack or something like that on it. security risk. So you simply type in a new name and any computer that this policy is assigned to will get that renaming of the local administrator account. And you can choose a password complex uh complexity. All sorts of different um options in there, password length, how long it has to be,

[1:52:23] post authentication, uh actions. And if we take a look at that, it says, "Use this setting to specify the actions to take upon expiration of the configuration uh configured uh grace period. If not specified, this setting will default to three, reset the password, and log off the managed account. Our options are as such.

[1:53:01] And we've got the post authentication actions. I'm sorry. Uh post authentication reset delay. And that's basically saying use this setting to specify the amount of time in hours to wait after an authentication. a successful authentication before executing the specified post authentication actions that we just set in the previous settings.

[1:53:33] If not specified, this setting will default to 24 hours. This setting has a minimum allowed value of zero hours. This disables all post authentication actions, so they won't take effect. This setting has a maximum uh allowed value of 24 hours. So if we go ahead and configure this, we can set the number of hours

[1:54:04] uh up to 24 that um the post authentication actions will kick in. And lastly, we have automatic account management enabled. Use this setting to specify whether automatic account management is enabled. If it is enabled, the target account will be automatically managed. Probably a good idea. If this setting is

[1:54:35] disabled, the target the target account will not be automatically managed. If not specified, this setting defaults to false. So, taking a look at those, it's either managed automatically or not. So, you want to plan a little bit, do a little bit of research on what you want to accomplish with um LAPs, but it's a very powerful way to protect um

[1:55:07] the local administrator account on devices. And going back to endpoint security, you'll see device compliance and conditional access listed here. I do not recommend configuring or managing those through here. Again, we'll do those through devices and we'll see that in our modules as we

[1:55:38] go through them. As you know, Microsoft has a million ways to manage stuff. sometimes and in this case I do not recommend managing them through here. Uh, and keep in mind anything that you manage underneath manage on the back end is still going to go to either a configuration policy, which all of

[1:56:10] these are, or a compliance policy or conditional access policy, which these are. So, if you configure them through here, it's still going to show up on the back end through the other underneath devices. Um, I do however recommend, as I recommended earlier, that any of the security stuff

[1:56:44] you do manage through here and not through devices. So lastly, let's talk a little bit about integration with Microsoft Defender for endpoint. So in order to integrate intoune with uh defender Microsoft defender for

[1:57:16] endpoint you have to click on this link which will bring you to the defender portal. look for the settings in Defender for endpoints and turn on the integration. And what that does is it allows your security settings that you're setting in here to be enforced by

[1:57:46] Microsoft Defender for Endpoint so that as devices get onboarded to Microsoft Defender for Endpoint, they'll get these policies. Now, I am having an issue in my tenant showing you step by step how to get there, but ultimately um because I had an old connector years ago that just never got removed and I don't feel like opening a Microsoft ticket to try to resolve it

[1:58:16] and and redo it. But ultimately what you're going to to to to get to is a point in settings where you're going to see u Microsoft offender for endpoint which I don't see here and then underneath there you're going to get to advanced features and underneath advanced features if you scroll down

[1:58:49] you will see. Where is it? Oh, now it's there. You will see it's not grayed out anymore, which is nice. I seem to have auto resolved it myself. you will see this option

[1:59:19] Microsoft Intune connection. You need to toggle that to on. Once you've done that, you can go back to Microsoft Defender for Endpoint inside of uh the Intune endpoint security. And you can turn on

[1:59:53] right here the Microsoft Defender for Endpoint to enforce endpoint security configurations. And then you're going to save. And what I'm seeing right here is describing why I cannot toggle these uh other options on right

[2:00:24] now. But when the connection status comes back up and running and synchronizes, I should be able to toggle those on those additional settings. And that wraps up our tour in the intoune portal of the endpoint security console. And now in the portal tour, we move on

[2:00:58] to reports. There is really nothing to say about the reports panel other than it's an all-in-one place where you can go to generate reports and download those reports for any of the components that we've already talked about device management and endpoint security.

[2:01:30] So for instance, if we went to device configuration and wanted to generate a report on uh any configuration um policy that we've done on the summary tab, if you've never generated a report for all the for example device configuration policies you'll see generate report. But

[2:02:02] if you're have already done it within the last 72 hours, you can click on generate again and it'll generate a report for all the configuration policies as a summary. Or you can go to the reports tab and click on policy configuration status.

[2:02:34] and choose reports based off of both the operating system and the policy type. So it gives you a lot of granularity in the reports that you want to generate. So in that sense it's more powerful than going to each individual component and collecting separate

[2:03:05] reports. And then of course you can choose to export your custom report and it will report it export it to a CSV. So we just click on yes and we see that the export has succeeded

[2:03:38] and it downloaded a CSV to our downloads folder. Now these reports come in very handy when you're dealing with Microsoft offender anti virus. Again, you've got the summary tab and you can click to generate a report

[2:04:11] on everything concerning Microsoft Defender antivirus. So, we'll go ahead and do that. And the summary is actually very uh very nice. It tells you um all the information that you would want to see in your environment. And

[2:04:41] um you can click on these categories and see some more information uh about the summary information on all all device statuses and and know scans pending reboot pendings um all that kind of stuff. Going to the reports tab

[2:05:11] allows us to get separate reports on both the anti- virus agent status and detected malware. So if we were going to take a look at, for example, detected malware, we have quite a few categories to filter on. Uh the severity, the execution state and managed by

[2:05:43] uh obviously configuration manager would be co-managed in tune. So let's say we wanted to see managed by in tune and severity is moderate or high or severe or unknown. we could go ahead and generate that report.

[2:06:19] And in my environment, I'm not really managing um a lot of computers, so I'm not getting um any data kicked back with that query. Um but do notice that you could export that to a CSV as well. And that's pretty much all there is to reports. So, let's keep moving along in our tour

[2:06:49] of the Intoune portal. Next on the list of our Intoune portal tour is the users menu. So the all users which it brings you to at the top by default really is the entra ID users on the back end. So

[2:07:21] there's really not a lot of difference um in this part between Entra ID and in tune until you dig a little deeper. So let's search for a user. So the landing page looks exactly like we see in Azure entra ID whatever

[2:07:52] you want to call it. However on the left hand side we see quite a few more options. One that I want to specifically point out is devices. Because if you notice in Azure and Entra ID, same thing.

[2:08:23] It's only going to tell you the user's primary device. However, with um something we're going to talk about an enrollment with device limit restrictions, you can go from the default of five enrolled devices all the way up to 15. And maybe you want to see all the devices that the user has enrolled. If you go through entra ID, you're only

[2:08:54] going to see the primary debug. So let's go ahead and take a look at the device list. So it's going to list every device whether it's enrolled or registered. It's going to tell me. So, here's the devices that I as this user have.

[2:09:24] It's going to tell me their enabled status. It's going to tell me the operating system in the version. And here's a really nice one. It's going to tell me the join type. Is the join type registered where the device is not enrolled. Is it enter joined

[2:09:56] or in the case of hybrid active directory um join environments you will see a separate listing that says hybrid joint. Now, you can also tell if they're enrolled in Intoune by looking at their MDM status. Anything that's enrolled in Intune will say Microsoft Intoune underneath MDM or

[2:10:28] if it's co-managed, it'll say co-managed or uh system center. Actually, I think it says config mgr for configuration manager for system center, SECM, MECM. A device will be registered and not enrolled if you have used applications to sign into your corporate account and authenticate through those corporate applications but not actually enrolled

[2:11:00] the device in in tune as a corporate device. There's a bunch of other useful information um in the users um per device or per user audit logs. You can take a look at the audit logs, troubleshoot any kind of lo on failures or anything like that or successes or

[2:11:34] suspicious activity. Sign in logs, same thing. Um, diagnose and solve problems. You can run some troubleshooters. Uh, do a new support request from there. You can also uh take a look at their assigned roles. It'll list all their assigned roles,

[2:12:06] um, any administrative units that they might be in, groups that they're in, applications that they're assigned to or that have actually been assigned to that user. Licenses authentication methods.

[2:12:36] You can do some of the reset password and reset um sorry re require multiffactor authentication methods from here. A lot of different stuff you can do from here. Uh very very useful. So that is the users menu on our intoune

[2:13:06] portal tour. So now we've come to the last component in the intoune portal tour that we're going to discuss and that is tenant administration. on the tenant status underneath the tenant details tab. There's not a

[2:13:36] lot we can do there. It's just mostlyformational um stuff we can check on our Intune uh tenant status. Under the connector status tab, we will find information on the status of any connectors that we have enabled in in tune to other services

[2:14:07] in Microsoft or any other services. It will give us a status whether it's healthy, warning or error. and it'll give us a timestamp as well. So, for instance, I can see that there's a warning right here on the Microsoft Defender for Endpoint Connector, which we've already discussed. And I can click on it and get a little more information and possibly configure uh those

[2:14:38] components and do a refresh or a delete and then reinstall the connector. So let's go back to tonet admin. We're not going to discuss every uh menu item in here. A lot of it is advanced stuff. Um that takes, you know, separate training or indepth uh

[2:15:11] discovery and um videos to to to really get into the meat of it and very specific scenarios, but there's a few that I want to go through. But before we go on to those other ones, let's just not forget to take a look underneath tennis status. Tenant status um at service health and message center. It's nice to be able to get a um uh a

[2:15:43] view on all of the service um health information related to Intune all in one place. So, we can scroll through here. We've got service health, issues in your environment that require action, message center, and underneath the message center, there's going to be all the information for planned changes, um,

[2:16:15] new settings, any of that kind of stuff, reminders, all that stuff. plan for changes, updates, those kind of things. So, it's good to review those on a normal basis so that you know what's going to be changing in in tune and patches and all that kind of stuff. Let's move next to connectors and tokens.

[2:16:46] most commonly if you're in ju just a few items uh if you're in SECM MECM uh configuration manager you're going to find your connectors in here in the status my environment is not using that so we're not going to find the connectors but that's um a very common one if you're in co- management mode with um the MDM authority being co-management and tune.

[2:17:18] If you are using Apple Business Manager and with Apple Business Manager, you are using the volume purchasing program with VPP tokens. You will need at some point to get in here to get your VPP tokens. Um, again, in my environment, I'm not using that. We'll talk a little bit about Apple Business Manager and Samsung Knox uh admin portal when we talk about

[2:17:49] enrollment. Um and also we'll talk about manage Google Play and enrollment and if you're using a enterprise solution um with Samsung Knox or without it um you're going to want the manage Google Play. So if we go to manage Google Play uh to deliver our apps

[2:18:19] then we can check on the status of the connector to manage Google Play and uh pretty much that's it. I mean you can define scope tags if that's necessary in your environment. So let's get out of connectors and tokens and go back to tenant admin. And now let's focus on the enduser experiences sections,

[2:18:51] the menu items underneath there uh for the remainder of our tenant admin section of the in tune portal tour. So let's go ahead and take a look uh first at customization. You can create and assign any number of policies by creating uh hitting the

[2:19:21] create button. Notice what it describes up here as far as customization. You can customize branding, support information, and other components of the user experience. And there's a hyperlink there for preview customization on the company portal website. The default policy applies to all users and devices. You can edit it, but you cannot delete

[2:19:51] it. In addition to the default policy, you can create up to 25 more policies. You can assign them to users, I'm sorry, user groups, not device groups, and they override the default policy. If you assign more than one policy to a user, they'll only get the first one, and that's according to priority. But in this case, we're just going to take a look at editing the default policy for

[2:20:23] all users. So, we'll go ahead and click on that. We'll go ahead and click on properties and we'll take a look at the settings by clicking on edit. And uh they're all pretty self-explanatory. In the branding uh page, you've got the organization name, you've got the color, standard or

[2:20:55] custom. as you clicked on custom. You could choose um a hex uh color. Um of course you want to put your organization name probably in there so they know it's legitimate when uh in tune is pushing stuff or they're going through an autopilot configuration makes it a little more legitimate and identifiable. um showing header, organization name

[2:21:26] only or logo and name. So if you choose a logo, if you choose a logo um that logo will appear along with the organization name um or just a logo. A few options there. Um if you do choose that option, you have to upload the logo. tells you right here what the dimensions are, all that kind of stuff. Um,

[2:21:57] you know, you just basically read through all this stuff and figure out what you want to look like for your uh branding on your company website for in tune. So the support information is pretty important because that will appear in the company portal app um so that users can identify the contact information for support. So you

[2:22:27] want to fill that in. Scrolling down and I keep talking about the uh company portal app and we really haven't had a chance to discuss that yet but when when we get into app deployment we'll talk more about it. It's required for enrollment of devices. It's the broker app and it's also the app delivery

[2:22:57] application that shows up in Windows and iOS and Android to deliver apps, but you have several options on how uh that's going to work with device enrollment. Um, you know, I'm not going to go through each one of these, but um, these are all in the uh, customization um, part of the T admin. Um,

[2:23:30] a lot of different options. You're just going to have to choose what you want for uh, customization in your tenant. So, let's cancel this. Let's go back to tenner admin and we will choose terms and conditions. So as you see with the the uh the the

[2:24:02] brief description up here, don't dismiss this. This is very important. um you may have compliance regulations that require acceptance of terms and conditions um depending on your industry. So the terms and conditions will show up before the device enrollment to make sure that they accept those terms and conditions. And so this is where you specify them. So basically it says satisfy uh stricter

[2:24:35] compliance requirements and improve the enduser experience with the new Microsoft Entra terms of use feature. Typically we just have one for the whole organization but technically you could create several and assign them as needed. uh if you had separate needs for terms and conditions for separate parts of your organization.

[2:25:07] So let's take a look at an example that I've already created for my tenant on terms and conditions. And if we go to properties and edit for an easier view, here's what we would configure in a policy for terms and conditions. There is the title

[2:25:37] which will show up uh during the in the title bar during the terms and conditions that shows up during the company portal app installation or other parts. There's the actual full terms and conditions that they will have to accept. And then there's a summary of terms that gives them a brief uh summary. There's also

[2:26:09] a selection box that says requires require users to accept, reaccept, and increment the version number to two if you change it. Full transparency here. What I typically do is I go to chat GPT and I say create me a terms and conditions for intoune with a title terms and conditions and

[2:26:40] summary of terms for whatever industry it is and I'll give the company name and I'll get a template and I'll put this in uh the output into this template and I will provide provide it to the customer, but the customer will have to review it according to um their policies, their corporate policies, and probably have to revise some of it, but it's a

[2:27:10] good way to create a blanket template to start with. So, I'm just going to scroll a little bit so you can see what that template looks like from chat GPT.

[2:27:42] And that's pretty much it for um the terms and conditions. So, let's go back to tenant admin. That wraps up our tenant admin uh tour on the intoune portal tour. So, let's start digging into some of the modules that we identified. we discuss

[2:28:13] and talk about specifics. Let's jump right into it. Okay, great. So now that we have the intoune portal tour and fundamentals covered, we can start taking a look at some of these components at a deeper level, a deeper dive and understanding them a little better with some more um detail.

[2:28:43] We need to start at the beginning with enrollment. So we're going to go to devices. and then underneath device onboarding enrollment. But before we dig into each one of these specific uh components for enrollment, types of enrollment, all that kind of stuff, we

[2:29:15] need to have a fundamental basic understanding of how enrollment works and our enrollment options. Windows devices can be enrolled manually or through autopilot or group policy. You can also enroll Mac OS, iOS, and Android devices. During enrollment, intoune installs a mobile device management MDM certificate on the

[2:29:47] enrolling device. On Androids, that's automatic. On iOS devices, you have to create an Apple push certificate. We'll see that the MDM uh certificate communicates with the intoune service and enables intoune to start enforcing your organization's policies like enrollment policies that limit the number or type of devices that someone

[2:30:18] can enroll. compliance policies that help users and devices meet your rules, configuration profiles that configure work appropriate features and settings on devices. Now, we took a look at uh compliance policies and configuration profiles in our intoune portal tour. So we should already be somewhat familiar with those but we will dig deeper into

[2:30:49] those in subsequent modules. So we need to talk about how does intoune actually accomplish technically uh managing the device itself. For devices that enroll it uses something called the company portal app. The company portal app is the enrollment broker for both corporate and BYOD bring

[2:31:19] your own device personal devices. It manages and allows secure access to corporate apps, corporate data, and corporate resources on devices, whether they're corporate devices or personallyowned BYOD. So, we'll talk a little bit more about enrollment profiles, uh, corporate versus BYOD. Um, but what you see right here is a

[2:31:52] BYOD device. And when you enroll with the company portal app, it's going to, at least on the Android, give you two profiles, a personal profile and a work profile. So in essence what it's doing is it's silo uh siloing your data your personal data away from your corporate data into separate profiles your personal

[2:32:25] with all your personal data and your personal apps and work all of your work data and work apps. So you might have Outlook in both prof profiles and your Outlook profile is tied to your personal account in your personal profile and your work account in your work profile. If we take a look at the company portal app,

[2:32:58] what you'll see is your devices listed there and you can get some information on the management of your device and compliance status. And you could always sync um by uh check device settings. But notice here the ownership type is personal, which means this is my own device, but I have a work profile on my BYOD personal device.

[2:33:31] And it gives you some options, tells you about the uh compliance um status, and you can always sync uh down below. And you know, that's the basics of the device details. Going back If we look at the menu and if we click on get apps, we would normally see a list of

[2:34:02] available apps and installed apps here, but in my environment, I just haven't done that. So, um, we're not going to go through that. But I just want to give you a demonstration of the company portal app and the personal and work profiles at least on an Android device. So let's talk a little bit more about enrollment of devices

[2:34:32] and distinguish between how corporate devices are enrolled and personally owned devices BYOD devices are enrolled and some differences between the enrollment types. devices enroll either as corporate or personally owned BYOD. The benefit of managing corporate devices is that it enables more device

[2:35:04] management capabilities than if it were uh a BYOD personal device. you can't manage as many um features on a BYOD device for obvious reasons. Regarding corporate devices during enrollment in intoune automatically assigns corporateowned status to devices

[2:35:35] that join to Microsoft Entra, Entra ID, Azure, whatever you want to call it, via one of the following methods. either a device enrollment manager account which uh is commonly uh referred to as a DEM account on all platforms. Um, but most commonly you're going to find

[2:36:07] that they're enrolled through a profile with Apple uh device enrollment program for iOS or iPad iOS such as Apple School Manager or Apple Business Manager or Apple Configurate uh Apple Configurator or Knox mobile enrollment for Samsung devices, the Knox admin portal.

[2:36:40] Other methods that would enroll it automatically as a corporate device is Windows Autopilot. No, I have a whole separate video going in depth on this and uh if you're interested, follow the link below. It's really involved. It's beyond the scope of this video. also

[2:37:11] a hybrid Azure AD join between active directory and Azure/entra ID and Azure virtual desktop deployment another in Android enterprise management solution or an AOSP Android open-source project management

[2:37:43] enterprise solution. So basically on the Android side if you have an enterprise management solution where you are working with the service provider such as T-Mobile, Verizon, AT&T to purchase the devices and select the option to um have an enterprise

[2:38:13] management solution built into that then you you would have the management solution to enroll those devices from those enterprise management portals and create a profile in in tune to import those devices and create a profile to um assign those devices and all that kind of stuff. Uh same thing with uh the iOS and iPad OS, Apple Business Manager, Apple School

[2:38:44] Manager, uh etc. Those are all solutions that would automatically identify and label those as corporate devices without any manual intervention. Alternatively, you can manually assign corporate devices by using

[2:39:14] corporate identifiers, and we'll go over that in just a little bit, or changing the device type per device post enrollment on Windows devices. Anyways, for personally owned BYOD devices to enroll in Intoune, they would have to manually install the company portal app for iOS and

[2:39:44] Android. in case that you didn't use any of the formentioned um enterprise solutions. And I do have in-depth videos on this. So check out the links below if you're wanting uh a little more information on how to do that. And for Windows, you can manually join to Entra via the

[2:40:16] settings applet and access work or school to enroll your Windows device manually. Now, all this talk is great for enrollment of corporate or personally owned devices where the user accepts and wants to enroll their device in the corporate environment. But suppose the user wants access to

[2:40:47] corporate uh data um and apps but does not wish on their BYOD device to enroll it in any sort or fashion into in tune for any sort of management on the device itself. So for BYOD users who do not wish to enroll their devices in in tune for management in the corporate environment yet still

[2:41:17] need to access corporate resources on their BYOD device. You can deploy ma'am Microsoft application management policies without enrollment which is also known as ma'am we ma'am without enrollment. This allows you as a corporate owner to your proprietary and sensitive data to

[2:41:49] manage and manage the applications and protect the flow of corporate data within those applications without managing the device itself. And we will talk more about this when we talk about the um uh ma'am in the subsequent module. So we've already covered underneath enrollment options both automatic enrollment and CNAME

[2:42:23] validation underneath the portal tour all the basic settings underneath there because there's not much to it. We'll now cover most of the remaining enrollment components which warrant a deeper discussion. Device platform restrictions allow you to configure and restrict

[2:42:53] which platforms can enroll in tune based upon platforms which are basically the operating systems. corporate versus personally owned devices platform versions and manufacturers. As with most policies in intoune, you

[2:43:24] can create um a custom policy, but in this case and in most cases, uh the default policy is the only one that you need to modify. You can't delete the default policy, but you can modify it. If you create custom policies and assign them to specific entra ID groups, then the custom policies would take precedence over the default policy and you could adjust those um precedence

[2:43:56] um priorities once you create them. But we're just going to assume for the sake of demonstration that we're only going to have the default policy for all devices and users in our organization. Now notice at the top you can create separate policies for enrollment restrictions for each platform. haven't seen much of a need to do this unless um again you need separate

[2:44:27] policies for separate separate um types of platforms and separate um devices inside your organization. The default enrollment restrictions policy includes all users. So, we're going to take a look at that one. So, if we go to the properties of the default enrollment restrictions and we

[2:44:58] take a look at um edit and see what we can configure, notice that we can set uh restrictions um based upon the each individual platform in the default policy. And that is really to say the operating system itself. When we take a look at platform

[2:45:28] that is referring to corporate devices. However those corporate devices are enrolled. Now remember for Android and iOS the only way the only ways to identify them as corporate devices is for instance with iOS you would have to use Apple business manager or Apple school manager to enroll them initially and

[2:45:58] they would be identified as corporate devices. And for Windows, you would have to um go through one of the enrollment procedures we talked about earlier like autopilot or manually going through the enrollment process or bulk provisioning. Alternatively, like we discussed earlier again, you could go into each device and change it from on the properties from personal to corporate.

[2:46:30] But that's what the platform column is referring to is corporate devices. Are we going to allow corporate devices, block them? In most cases, I would think we would want to uh allow corporate devices for sure except for maybe Android device administrator because that's deprecated and old. We can manage the versions on Android and iOS.

[2:47:02] Uh not for Mac OS or Windows. I'm sorry, not for Mac OS, but for Windows. So, we basically say we're not going to allow any legacy operating operating systems that we cannot support to enroll in tune. So that might be a good measure to say, "Hey, listen. We don't want any of this legacy stuff. It's going to be a support nightmare. So we're just going to block it right off the bat." And then if a user tries to enroll themselves manually, well then they they're going

[2:47:34] to have to go to support and have a conversation about that. And then there's personallyowned BYOD. If you're in an environment that doesn't allow BYOD, then you're probably going to want to block all the BYOD devices, at least for the mobile operating systems. Maybe consider blocking Mac OS if you're not a Mac environment. And maybe even um Windows, but that takes careful consideration because then

[2:48:06] you're going to possibly run into issues when people want to work from home on their home computers. And then we have device manufacturer for Android only. At this point we can specify which manufacturer we want to allow and which ones um well specifically which ones we want allow. And that's it.

[2:48:38] And that is all there is to enrollment restrictions which on the landing page is called device platform restriction. So we also have a device limit restriction right there. Device limit restrictions allow you to

[2:49:09] specify the total number of devices any single user can enroll in in tune. The device uh default is five and the maximum is 15. So this is a combined total between all the different types of devices. So, let's say they had um two Android phones or an Android and iOS, a Mac, an iPad, a Windows device,

[2:49:42] um maybe a work Windows device and a home Windows device. Um those would all contribute to the um uh total. So, the minimum is zero. I don't know why you'd want to put it at zero unless you didn't want um them to be in uh to be able to enroll at all. Uh the default is five and a maximum is 15. Uh that's just an intune Microsoft limit that they cannot with the license uh enroll

[2:50:16] more than 15 devices per user. So if we take a look at that, it's very simple. There's not much to configure. Go to properties and edit limit and simply drop down 1 to 15. I guess zero is not in there. Interesting. But notice you can't manually type in anything. It goes from 1 to 15.

[2:50:51] Jumping backwards for just a second, co- management settings that has to deal with SECM, which is now called MECM and its later versions. That is so far advanced and so far beyond the scope of an intune um beginners training or basics trainings and fundamentals. Um I will be doing some future videos on SECM. I have some already. Um, but as far as co- management goes, um, there's

[2:51:22] a lot to that. You're not going to get that in in in a a reasonable amount of time in the this sort of video. Pretty much the same thing for Windows Hello for business except that if you configure this on a basic level here,

[2:51:52] this is just for Windows Slow for business as an enrollment type when your devices are joined directly to Azure AD entra ID. It is not for a hybrid with active directory AD environment but it's a pretty simple deployment with uh Azure AD join devices but a lot

[2:52:23] to consider. Again look for a future video on this. I will be diving into Windows Hello for Business. don't have a video on it yet, but keep an eye out for that. Um, there's a lot to architecture and deployment on that. So, uh, you know, we're not going to get get into all that at this point, but if you're doing just straight Azure AD, enter ID, uh, devices, you can configure that here and probably figure out, uh, the the,

[2:52:55] you know, the minimal options and that is an enrollment option. Scrolling down to Windows Autopilot. Again, I have a whole separate video on this. Very complex. Lot to talk about. My video I think is very advanced. Is on this is about an hour and a half plus. Um probably more

[2:53:28] than that. on all the considerations for Windows Autopilot. Windows Autopilot is basically, you know, how do you configure out of the box experience when a when you want to re uh deploy for the first time a a device, a Windows device to a user, have it join either Active Directory hybridly or to to enter ID or just straight Azure ID join with authentication

[2:53:58] and apps that you push and configuration and the out of the box experience of OB that they're going to see and reporting on that all that kind of stuff. I think I've already provided a link to that when we went over the portal tour. If not, just check my channel for uh the autopilot um video.

[2:54:28] So, let's scroll back up to the top and look at the other available tabs underneath enrollment. Taking a look at corporate device identifiers, what we have there, and we'll jump back to Apple and Android in just a minute. So, corporate uh device identifiers are a

[2:54:58] way to ensure that corporate devices are marked as corporateowned as soon as they enroll by adding their corporate identifiers ahead of time in the Microsoft Intune admin center. The benefits of managing corporate devices as we discussed previously is that they enable more device management capabilities than personal devices.

[2:55:29] For example, Microsoft Intoune can collect full phone number and app inventory from a corporate device, but can only collect partial phone number and app inventory from personal devices. And when you get into, you know, things such as re uh wiping a device and locating a lost or stolen device, those kind of things. Now, if you're using a third-party

[2:55:59] um enterprise management solution like on the iOS side, Apple Business Manager or Apple School Manager, you wouldn't need this. They will automatically enroll as corporate devices. Same thing with Samsung Samsung Knox. Um, but if you're not using or subscribing to one of those services, this is a way to identify the devices um before they enroll so that they automatically enroll as corporate

[2:56:29] devices and you can manage them as such. So, it's not too complicated. You would go to add of course and you can either manually enter the identifier and the details. So underneath the identifier you can select the either the serial number or the EI from the device itself.

[2:57:01] And this is the way to do one offs or just you know a few at a time. However, we can also add through a CSV file for bulk enrollment of corporate devices all at once. Now again you still have the

[2:57:32] IMEI and serial number but for Windows you have an additional option manu manufacturer model and serial number. Um so you have to select an identifier type and then you have to uh select the file that you've created ahead of time and so you might be able to script this with Windows for example to export to a CSV. Now, it'll show you if you hover over the uh

[2:58:02] import identifiers what the format of that CSV file has to be. So, it tells you for IMEI or serial number what the column headers need to be. um for example. And then we have device enrollment managers commonly

[2:58:32] referred to as DEM accounts. So a device enrollment manager user account is a nonadministrator user who can enroll devices in in uh dem users are useful to have when you need to enroll and prepare many devices for distribution.

[2:59:03] People signed into a DEM account can enroll and manage up to 1,000 devices, while a standard non-admin account can only enroll 15, which we saw earlier with device limit restrictions. So the end user themselves can only enroll 15 devices whereas you can specify a non-admin a non- global admin

[2:59:33] or some other specialized role that an intune as such as in tune administrator that um as a dem account can enroll up to a thousand devices. So, in smaller organizations where you maybe only have that amount or less, um you might want to consider a dem account so that the user

[3:00:03] um doesn't have to go through the enrollment process. you could have a an allocated possibly like a tier one kind of account um an MSP that is allowed to enroll the devices and then send them off to the user. So there's a couple of requirements for a dem account. A dem account requires an intune user or device license. So an in tune user

[3:00:33] license or device license and of course an associated Microsoft Entra/Asure user account. So a device enrollment manager a DEM user can use the following methods to enroll devices in in tune. They can use autopilot on behalf of that user. They can do Windows devices bulk

[3:01:06] enrollment via something called Windows configuration designer and through that process create a provisioning package for bulk deployment. They could use the their dem initiated account via the company portal by manually enrolling each device through the company portal app. Or they could use their dem initiated

[3:01:36] account via Microsoft Entra join which is basically going to the settings and then going to worker school and then adding the device as an enrolled device through their DEM account. So going back now to Apple and clicking on those enrollment options.

[3:02:08] In order to enroll and manage any Apple devices, you're going to have to create an Apple MDM push certificate which will securely communicate between um you know Apple services and in tune. Now, it's important to point out right off the bat that um the certificate has to be uh renewed

[3:02:41] uh once a year. So, when you create the certificate, it's only good for one year and you have to renew it every year. So, it will tell you right up here when the expiration date is once you create it. And you're going to need a corporate Apple ID to sign into to create this Apple

[3:03:11] certificate on the Apple land. So the first step in any certificate uh creation is to create um a certificate signing request a CSR. So we're going to have to do that first. and it'll go to your downloads folder. You'll see see the CSR um for encryption. Then you have to create your certificate

[3:03:41] by logging in with your Apple ID to the Apple portal. And then if it's the first time you're creating a certificate, you're going to click on create a certificate accept. And then you're going to choose that file, that CSR file

[3:04:12] that we had earlier downloaded. And then we're going to click on upload. And at this point, the certificate is ready to download. And we would click on download when we're creating a new certificate. And that will go to our downloads folder

[3:04:43] as well. However, the process is very similar up to this point. If we were renewing, we would simply click on the renew button for the existing certificate after the one-year expiration.

[3:05:13] In any case, once we've downloaded our certificate, whether it's created for the first time or renewed, we're going to go back to Intoune and we're going to scroll down, type in our Apple ID, and then select that push certificate that was downloaded. And then everything's good. What you'll see up top

[3:05:45] is this whole section that tells us first of all, okay, it's active when it was last updated, Apple ID, serial number, all that stuff. but days until expiration and the expiration day. And that's creating an Apple Push certificate that's needed for

[3:06:15] um enrollment and management of the device. And I do have a whole separate video on the company portal app um installing it to manage the device which is shown down below. So, if you're using Apple Business Manager or School Manager to enroll your devices and basic basically manage your

[3:06:45] devices through um both Apple and Intune, you're going to want to go to enrollment program tokens. Click on that and then go to create. Click on I agree. And there's a whole process to this.

[3:07:16] It's a little bit again complex and advanced. And you're going to have to create enrollment profiles on the Intune end as well and do some stuff on the Apple Business Manager end um to make this work and to get the devices imported way beyond the scope of this video. Um check out uh future videos because I will be creating a video on this. But um at this point that's how you get to that. But we're not we're not

[3:07:48] going to run through all of that in this in this intune beginner's guide um video and fundamentals video. If you want a step-by-step guide on this, um I've included the link below to um to get started on that. Moving on to Android now.

[3:08:20] We click on that. So let's start with manage Google Play. What manage Google Google Play allows us to do is to deliver and deploy apps from the manage Google Play Store so that you can authorize the apps that you want and deploy those apps as either required or available to enduser

[3:08:51] devices. You will need either an enterprise um Google account for the manage Google Play Store or now Microsoft allows for an enter ID admin account to be used for manage Google Play. So you have to set up the connector first. And

[3:09:22] in order to do that, you can click on the learn more button right here. And that will bring us to a page that displays all the information on how to connect in tune to your uh Google manage play store. Uh pretty straightforward. Not a lot to talk about in here. But you can follow this simple procedure and connect in tune to your

[3:09:54] manage Google Play account either with an enterprise Google Play um account or there are steps to use an enter ID account. Now instead of a Google uh manage Google Play enterprise uh account underneath enrollment profiles we have several options. We have personallyowned devices with

[3:10:24] work profile. Now we um spoke about this earlier with the personal profile and uh the work profile. This is an option for BYOD devices. But if we click on this, it basically says that you have nothing more to configure that um it's pretty much automatic. So all that really happens is that when

[3:10:55] a user logs onto an application with the corporate credentials, it creates a work profile and isolates silos that work data from the personal data and creates a work profile on top of the personal profile, but it still enrolls the device. Next we have corporateowned dedicated devices. And if we take a look at that,

[3:11:26] what does that really mean? This is really designed for kiosk devices. And with kiosk devices, the end user uh if it's corporate device has almost no control, no access to the settings. It's basically only what you give them control over um for apps and access in this mode. Be very careful if you choose this mode because you cannot

[3:11:57] um deploy configuration or compliance policies. So this is only really for let's say the scenario is you have a front desk Android tablet and you want to use it as a kiosk device that that's the selection you'd want to choose for this type of scenario. I wouldn't use it for enduser devices that the end user has to

[3:12:28] interface with multiple applications and and settings and those kind of things. The most common one is corporateowned fully managed user devices. So this is for corporateowned devices that are fully managed by the corporation. So we will click on that and take a look at what our options are. Now keep in mind we're still in

[3:12:59] enrollment. These are all different enrollment types that allow different types of access to the device or the applications depending on which kind of policy you deploy during enrollment. So I have already created a policy for fully managed corporate user devices and I want to take a look at that.

[3:13:36] When we take a look at properties pretty much there's not a lot to define in here. um just basic stuff really everything happens underneath token. So my recommendation is to use Samsung Knox compatible devices only. I would not use the Android open-source project type of devices. And when you go to configure the Knox

[3:14:09] Samsung Knox admin portal to import devices and connect it to Intune, there's going to be a procedure, but you're going to need this token that you created during the policy when you created that policy. And that's the token right there. So, the Samsung Knox Enterprise Management Solution is way beyond the scope of this video. Um, a lot of stuff

[3:14:39] you have to do, but take a look at the link below if you want some more information and step by step on how to do that. But just realize that this is where you're going to get the token from. um when you need to go into the Samsung Knox portal and provide the JSON um syntax with the token in it. And then there's a whole procedure for

[3:15:09] importing and syncing devices. But you also have the option to just enroll your device with a QR code and you can scan the QR code um by using the QR code shown here. So you can provide that to users securely to manually enroll as a corporate um own

[3:15:39] fully managed device either in the scenario that you're using Samsung Knox or you are not using that enterprise solution but you still want to enroll as a corporateowned fully managed device uh manually. The corporate own devices with work profile gives a little more liberty to the end user to have control over your corporate

[3:16:11] devices with their work uh profile versus their personal profile. So they could do more with their personal profile. If it's a corporate device, in my opinion, uh this is not not an option. Uh I don't recommend this. Um as a matter of fact, I've never deployed this. Um quite honestly, with corporate devices, you want to use this option. That's it.

[3:16:41] And that's all there is to enrollment. We've wrapped up this module. So now we're moving on to compliance policies. With compliance policies, the main idea is to ensure that devices that gain access to your corporate systems and corporate data are secure and won't pose risks to your corporate environment. And

[3:17:11] in this this case, we're mainly talking about Microsoft 365. For instance, with compliance policies, you typically want to require the following minimal validation checks on the device before flagging it to be marked as compliant or non-compliant. Not jailbroken for iOS. Not rooted for Android.

[3:17:41] you want to require encryption. On iOS, that's automatic because iOS is already encrypted, but on Android, uh, it's an option. You want to set the password and pin settings on mobile devices and you want to ensure uh the threat level protection. It's important to understand that compliance policies do not enforce any

[3:18:13] configuration settings. It's simply a validation checkpoint. Configuration policies on the other hand and force settings on enrolled devices. For configuration profiles, I'm sorry, for compliance policies, you want to have a balance between compliance checks and the user ability to proceed to access corporate data.

[3:18:45] Recall that compliance policies do nothing on their own other than mark the device as compliant or not. However, this flag can be used with conditional access policies to block access to your Microsoft 365 environment where your corporate data lies if a device is marked as not compliant.

[3:19:15] Thus, conditional access policies become the gatekeeper to your corporate data based upon one of the conditions that you can choose being compliance policies whether a device is marked as compliant or not. So, let's poke a little deeper into compliance set uh settings and policies. We're going to find those underneath

[3:19:45] devices. Then scroll down a little bit and find compliance. Click on that. And the first thing we're going to take a look at is a tab on top that says compliance settings.

[3:20:18] And this is very important not to skip. By default, Microsoft has your compliance settings marked to say mark devices with no compliance policy assigned as compliant. which is ridiculous because if you don't assign a compliance policy, all devices are compliant and it defeats the whole purpose. So the first

[3:20:49] thing you want to do is change this to not compliant. If it doesn't have a compliance policy assigned, then it's not compliant. Second thing you want to do is determine the valid uh validity period uh and number of days that the device is compliant before it has to check back in uh to make sure it's still compliant. So

[3:21:19] if we if we read the information on this, it says specify the time period in which devices must report the status for all received compliance policies. uh because you can have multiple compliance policies. We'll take a look at that in just a minute. Devices that do not return the status within this time period are treated as non-compliant. The default is 30 days. So, you can adjust that as needed for your corporate environment.

[3:21:50] So, let's go ahead and take a look at policies and how to create them and what settings are inside those. We'll click on create policy and then we will choose our platform. Um, for this demonstration, we will choose Android Enterprise.

[3:22:20] And we'll do fully managed, dedicated, and corporateowned work profile because that'll have the most settings available to control the device or or to detect on the device. And we'll hit create. Give it a name.

[3:22:53] click on next and then take a look at the available categories and settings. So underneath Microsoft Defender for Endpoint, um unless you're actually deploying the Microsoft Defender for Endpoint um application to Android, this is going to be pretty much um irrelevant. But if you do then you can um just select the

[3:23:25] um risk level that you will are willing to accept for the device to be considered compliant. And you can uh click on either one of these um to get a little more information on those risk levels. Under device health, we're going to see a few options. I always recommend blocking rooted devices. On iOS, there's

[3:23:56] a similar setting for jailbroken devices. It's a risk to your um environment to have those kind of devices um to be able to authenticate and access corporate data. Now this next setting has to deal with third-party anti virus um systems, anti-malware systems that you have already um created a connector to in in

[3:24:26] tune so that it can um assess and gather the information to make this um assessment. Um and if we take a look at the article on that um Intoune can integrate data from a mobile device threat uh defense vendor as an information source for device compliance policies and

[3:24:58] conditional access rules. Um, you can use this information to to help protect corporate resources like blah blah blah blah blah. Um, you can use uh in tune can use the same data as a source for unenrolled devices using intoune app protection policy. So you have to create a connector. Um, if you take a look down here, um, there's some more information on uh the mobile def uh threat defense

[3:25:29] connectors um, and the status. But what we really want to take a look at here's some of the information it gathers, how it works. But, uh, here's what I wanted to show you. Uh taking a look at the connectors that you can um integrate with in tune are listed uh towards the bottom of the page. Here are some of the ones that you can uh create a connector for that

[3:26:00] automatically connect from your third-party management solution into intoune and it'll just uh sync that data on a regular basis. So going back to the compliance settings underneath this policy, unless you have a connector, do not configure this because um it won't be able to evaluate

[3:26:31] um that third party system and it will probably fail compliance. You can also configure uh Google Play verdict to check integrity. It's up to you. I don't usually do that. Again, it this is just let's get it through the door and configure the device afterwards. If we expand device properties, it's really just version stuff. I typically don't worry about that for compliance

[3:27:03] settings. Remember, you can control that through the platform restrictions underneath enrollment underneath system security. Scrolling down a little bit, you probably want to require a password to unlock the mobile device just as a

[3:27:33] basic security measure um to get through the door again. And put some information in here. just probably very basic stuff to get through the door because uh later on you you you can once it gets through the door and en rolls and they authenticate you can push these settings to a more strict value through configuration policies. So I wouldn't go too heavy on this.

[3:28:03] Maybe just do something simple like this. just require a numeric password length of four and maybe not even do any of the rest of this stuff. Probably would require encryption. And that's pretty much it. Just double checking our settings.

[3:28:42] And then we're ready to hit next. We've got the automatic selection of mark the device as non-compliant immediately. Additionally, we would configure add the device to the retire list after 30 days.

[3:29:12] Then we would click next. Don't worry about scope tags. Don't forget to assign it to a certain entra ID group. So we're going to click on include groups and add groups. and then we will do the group. Now, remember when you're first rolling this out, you're going to want to test it and not roll it out to all production devices right off the bat

[3:29:45] or all users. And then click next and create. So, I want to show you a Windows compliance policy specifically for the reason of showing you how to create a custom compliance uh detection for third-party

[3:30:16] anti virus uh anti-malware which is very common request. It's quite a complicated procedure. We're not going to walk through um everything uh every single step, but we're going to walk through the overview and I'll give you a couple of helpful articles on how to perform it yourself. For a full stepbystep guide, visit this article, this website. It'll walk you

[3:30:46] through every single step along the way. Um, but I'm going to give you an overview so you have at least a general understand the of the steps that are involved. So, just go to the URL that I have listed above here to view the article and get the step-by-step instructions.

[3:31:20] In a nutshell, you have to do three things. You have to create a PowerShell script for detection. You have to create you know detection of the third party antivirus. You have to create a JSON file and then you have to create your Windows 10 compliance policy and in there you're going to specify

[3:31:50] a custom detection and specify the PowerShell script and the JSON file inside of that policy. So let's take a look at that. So, first off, you have to go to underneath compliance still to scripts. And underneath the scripts, we're going to have to create a script based off the

[3:32:21] information in the article and customize it according to your anti virus, anti-malware solution uh that you have in production. So you can see I've already created one and this is actually straight from that website just as a an example demo. So once you've got that script uploaded underneath devices compliance and

[3:32:52] scripts and you've got the JSON file created and somewhere accessible on your computer, then you can create a Windows 10 compliance policy with a custom detection script and JSON file defined for the anti virus uh part of that

[3:33:22] compliance policy. So we will go ahead and create a policy for Windows 10 and later and we'll do compliance policy and create. Give it a name.

[3:33:59] Click on him next. And then underneath custom compliance at the top here, we're going to go ahead expand that. We're going to say require. And then we have to do a discovery script, which is why we have to have that already uploaded, created and uploaded to select it. going to click on that

[3:34:31] and then it's going to want that JSON file. So, I have to find that JSON file. So, I'm going to go to find that JSON file. So, we will also have to select that JSON file correctly formatted. And when all that goes well, it'll look something like this.

[3:35:03] with the script and the JSON file being validated. Now, you could add um other settings as well in this compliance policy, the ones we talked about earlier, but uh we're not going to in this example. And then you would just go to the settings we talked about earlier for actions for non-compliance scope tags and assignments. Um, but

[3:35:33] that's the that's the really meat and potatoes of creating a compliance policy that's customized for third party anti virus anti-malware solution. Of course, you would target that for assignments to a test group and enter ID first before rolling out to production. But at this point, I think you're getting the hang of that. And then you rolled out to production.

[3:36:05] And that's it for our instruction and demo on compliance policies. So, let's move on to the next module. So now we are moving on to configuration policies and we're going to focus on uh corporateowned uh fully managed devices on Android with the device restrictions for this demo.

[3:36:35] So in order to get to configuration policies, we have to go to devices and then underneath devices, scroll down a little bit and we will go to configuration. We will click on create.

[3:37:05] And in this scenario, new policy and select platform. We're going to do Android Enterprise and the profile temp uh type will be templates. And we're going to choose a template under fully managed dedicated and corporateowned work profile for device restrictions. Notice there is also the one for personally owned work profile. It depends on your scenario. Uh fully

[3:37:36] managed uh dedicated in corporateowned work profile is going to have more options. You can control more over the device than if it's a BYOD personally owned device. So we're going to go through all the options or most of them anyways are pretending this is a corporate owned device. We're going to click on create. Give it a name. Click on next. And then we'll see all the um settings

[3:38:07] that we would have for corporate and owned fully managed devices which are going to be more than BYOD personally owned devices. We can control a lot more if it's corporate device. We won't go through every single one of these settings, but I want to give you an overview of the categories and what kind of settings are in here. Now remember, some of these settings um will control the applications, the corporate applications, but uh there will be more settings available in ma'am uh policies

[3:38:40] um if you want to control uh ma'am on top of the device itself. So ma'am is going to control the applications the work profile that have corporate data. So uh we might want to do both um a configuration policy and a MAM policy but um some of the settings in the device restrictions have a MAM effect.

[3:39:11] So it just depends on how you're going to do it. Um, if you don't intend to deploy MAM policies and only want to do device restrictions, then you'll have a limited set of uh, MAM controls. Uh, but if you want a full-blown set of controls on the corporate apps, then you would additionally deploy MAM policies on top of this or just not con configure the MAM policies settings in

[3:39:44] on the device itself and then control all of it through MA. It's just a matter of planning. So, under general, we're going to see um a whole bunch of stuff. Um it's going to separate it by category for fully managed, dedicated, and corporate owned worth profiles. And then you're gonna see categories for fully managed uh and dedicated uh devices.

[3:40:14] And then you know it it depends on how the device is enrolled for each one of these. Um, so depending on your device enrollment, you want to set the settings for um each one of these types of enrollments that you have chosen um in your environment. So, we've got screen capture, camera,

[3:40:44] um, you know, uh, default permission policy, prompt for the work profile, date and time changes, roaming, data services, Wi-Fi access, Bluetooth configuration, tethering, USB file transfer, external media, beam, developer settings, microphone adjustment,

[3:41:15] factory reset, um system update, all these are configurable. Um you know, and and if you choose to configure them, um you might have a subset of categories underneath each one of those. Um it it depends on on each setting. um you know volume changes, factory reset, status bar, again a lot of the same settings and this other type of profile.

[3:41:47] Um so you can you this is the this is the the most uh fully controlled profile where you can um or policy where you can control each one of the type of profiles. So, you would want to go through this and and and set each one of these settings. Locate device, power button, menus, system error warnings, notifications on the um you know, we used to call

[3:42:17] toast, those kind of things. Um you know this is very important to consider when you again have um regulation um requirements for things such as uh ITAR defires Fed ramp HIPPA

[3:42:48] NIST CMMC you may you want to make sure that you enforce these um compliance regulation requirements according to the standards that they require on your devices. So you you have to reference those requirements and make sure that uh each one of these settings is um um is is is uh addressing those and and

[3:43:18] accommodating those. Moving on, let's minimize the general category and go to system security uh threat scan and apps. Again, you might have to have those connectors to be able to do that device experience. Um I typically don't do this. Um, if you select kiosk mode, uh, basically locks

[3:43:48] the the user out of everything. Um, and Microsoft launcher is basically a min start menu. Um, unless you really want that. I don't typically configure this. Device password. Now again the compliance policy says well let's say that they just need a password on their device configured in a minimal um numeric fourdigit. We can go ahead after they get in and say well let's get a

[3:44:19] little stronger you know and that's where you would do all this um all all these kind of settings on the password power settings. Yeah, I think on Android that's kind of irrelevant. Um, other than time to lock screen. Um, users and accounts. This is kind of important probably especially if it's a corporate device which we're going over

[3:44:49] here. You want to consider your corporate policies and whether um users can add personal accounts to the corporate devices and whether they can remove the um uh corporate account that they log into. I would suggest um they cannot you block their user removal for the corporate device. If they have to do that, that's up to the administrator uh through intoune to do that. Um, and I would not allow personal

[3:45:21] accounts on a corporate device. If it's BYOD, that's a separate profile. That's different. Uh, those are all those kind of settings. applications. You have options for, you know, unknown sources, whether you can allow installation for them, updates, uh, Google Play stuff, all that kind of stuff.

[3:45:52] underneath connectivity. Um, you can do an always onVPN to enforce a VPN for uh access to corporate data and lockdown mode. again separate profiles um configurations depending on how the device is enrolled and you'd have to configure those for the type of enrollments that you've allowed or uh devices that have enrolled

[3:46:24] for each one of those profile password you can uh enforce um all the settings on this. Um and I would recommend doing this. That's a you know probably maybe a compliance uh regulation requirement. Um, so even though the

[3:46:54] um, uh, Intune compliance says, well, just to let them in, it's numeric for, here's where you can say after they get in, here's what we're going to enforce on the device itself, which is different than the application data in MAM. Then we've got the personal profile. Now remember the when you um have corporate

[3:47:24] devices and enrollment um you're going to have a work profile and a personal profile. Um and um when when you enroll, you can determine how much of that um is um available to a personal profile. But um with a personal profile, if it's a corporate device, you can control, you know, the camera and screen capture and those kind of things. Whereas with a BYOD device, if we were going to do a a

[3:47:56] device restriction for a BYOD device, we would not have as much control over the the device itself and this kind of stuff. And then this is helpful but you know um not necessary. Um this is information you can provide. And what what's going to happen here is in the company portal app that's installed on the device. This would be the information that we'd show in there.

[3:48:28] So that um if the user were in the company portal app and trying to find out who do I contact for help um it's just um it's just kind of useful information not required but um it doesn't hurt to put that in there. Device restrictions on iOS are very similar. On Windows, a little different.

[3:48:58] And of course, you would have to, you know, assign this to initially a test group, a pilot group, and make sure it all works the way you intended, and then roll out to production. In every environment, you should have a device restrictions prof uh policy for every type of operating system, iOS, Android, Windows um as a as a minimal.

[3:49:31] You can obviously create other types of configuration profiles, but um what you know it's it's kind of beyond the scope of this this uh this video. It's you know this video would be like 60 hours long. I mean, we can't we can't go through everything in um the types of

[3:50:01] configuration profiles, but just as a review, you could do Wi-Fi, VPN, certificate, PKS, um types of types of profiles. Um for the templates uh for Android Enterprise for Windows 10 later you're going to have um different types of templates

[3:50:32] all these different types of templates that you can do for Windows 10 and beyond. Uh a lot more that you can do with that. So just keep that in mind. But obviously we can't go through every type of configuration policy in all the settings. So I just want to give you demonstration of a typical type of uh configuration policy.

[3:51:02] And that concludes our configuration policy for device restrictions. Next we'll move on to endpoint security as far as configuring uh configuration policies. So let's jump into the endpoint security and configure a few of the security

[3:51:32] policies inside of there. We'll start off with anti virus and we will create a new policy. We have the options to create a policy for Windows, Mac OS, Linux, or Config Manager. We're going to do Windows as a demo.

[3:52:05] And when we select Windows, we have a few more options uh underneath the category for profile. Um the main one is to select the defender antivirus um category option and configure the antivirus um solution itself. the Microsoft Defender antivirus software, all the uh

[3:52:35] selections inside of there. So, we're going to go ahead and start that. We'll click on create. Give it a name and click on next. and we will see all sorts of options for the Microsoft Defender endpoint

[3:53:06] protection um component to Windows. Uh you've got archive scanning, behavior monitoring, cloud protection, email scanning, uh scanning of map network drives, um allow full scan of removable drive, scanning, intrusion prevention system, whether to allow it or not, scanning of all download files and

[3:53:36] attachments, real time monitoring, network files, um uh script scanning, whether to allow the user interface access to the defender settings and letting them um change those or blocking them out. Some resource um choices here and how to throttle the resources. Um check signatures before running scan.

[3:54:09] club block level. Uh different selections in there. Um days to retain clean mailware, disable full catchup scan. And by the way, you can click on any one of these information um areas and it'll tell you more information on here. So basically, you know, disable catchup full skin is like if somebody's been offline um do you want to disable it or

[3:54:42] um disable the disable which will enable it? Um, same thing with a quick scan, uh, CPU priority and other resourcing, enable network protection, and you can add extensions for exclusions, uh, file extensions, paths, and processes in here. Um, but you can also create a separate policy for that if you needed to separate those out for different types of

[3:55:14] uh groups that you want to target specifically. Like let's say you had a group of servers and you had a group of um desktops or more than one group of servers and desktops and you wanted to have different exclusions for those but you wanted to have possibly one protection policy then you could you could do those uh separately. We'll see that in a second. uh PUA protection, real time scan direction,

[3:55:47] you know, which way you're scanning files in and out, scan parameter, quick scan, full scan, scheduled scan. You click on that, you get um options for when to uh schedule it um by the uh I think it's by the minute. I forget. Yeah. 0= 12 a.m.

[3:56:20] 60 is 1:00 a.m. So it goes pretty much by the minute. Uh scheduled scan day. Choose your day time. Um all sorts of different options in here. You just got to look through them and choose them. I mean, there's nothing really tricky in here. Uh you've got your threat uh actions for

[3:56:52] high severity, uh severe, low severity, moderate. Um, and so you're going to choose from clean, quarantine, remove, allow, or userdefined or block depending on the severity level for each one of those. um some other stuff that you may or may not have to deal with um for HTTP and uh SSA SSH and

[3:57:26] TLS. Um platform update channel. Um what do you want your engine to be at? Security intelligent updates channel. um current stage or current channel. Let's see what else we got. And that's kind of all there is to this. You know,

[3:57:58] you can obviously have multiple policies and target different groups that might have different devices in them. And one common case is servers versus desktops or workstations, whatever you want to call them. Um maybe remote workers their laptops would be different uh policy. Um you take a look at an example what I've done down here

[3:58:28] settings I've created underneath defender you know um we'll just kind of scan through this really quickly. I won't read every single one of these but we'll scan through them. you get an example of what a basic um setting would look like. You can pause along the way if you need to. You know, obviously you want real-time monitoring, you know, script scanning and intrusion prevention and um email

[3:59:00] scanning. Those are all kind of standard stuff. Um check for signatures. Yes. To update those signatures before you run scans. um you know how many days you want to ret retain the uh mailware before it automatically deletes it you know quick scan uh 120 which I think is what shoot yeah 60 was 60 minutes said be 1:00 2 o'c 2

[3:59:33] am or something like that on Sunday I think Um for the quick scan, the regular scan is at 200 at minutes uh past midnight I believe. Um how often is the uh uh signatures are updated every 8 hours is what I selected. Allow on access protection. Yes. when users access

[4:00:05] files, you want them to to to be scanned. Um, and here's what I have set for um uh remediation actions just as an example. You don't have to go with those. Um sometimes uh people just choose quarantine for everything and that's avail valid option as well.

[4:00:39] Going back to anti virus if we create a policy for Windows and this time choose antibirus exclusions. We have the option to create a separate policy for exclusions. We wouldn't have to create them in the antivirus one. We could just leave it alone and create separate policies for exclusions depending on which groups you want to apply those exclusions to. And it's the same thing

[4:01:09] with the policies. You can create separate policies for certain groups of of devices. So, you know, if we just took a look at the settings here, um it's just those subset of what uh of the exclusion settings that we saw in the antivirus policy um in only those. And so, it's a quick and easy way to just define separate policies for exclusions and a way to keep yourself organized to

[4:01:40] realize, okay, wait a second. um which policies have which exclusions. So you can easily deploy them to different groups without being locked into the exclusions being uh part of the antivirus policy itself to isolate those settings and apply them granularly and independently of the antivirus policy itself. So that's a a nice uh feature to have.

[4:02:11] Now we move on to disk encryption. When we go to create a policy, we have the options for creating a Windows, which is Bit Locker, or a Mac OS disc encryption policy. So, we're going to choose Windows for this demo and we're going to use Bit Locker

[4:02:45] and click on create >> name. next. And then we're going to see a whole bunch of uh categories uh each of which has settings. So for Bit Locker uh itself, the drive encryption, uh settings for the type of encryption, those kind of things, and then different

[4:03:15] settings for the operating system drives, fixed data drives, and removable drives. So, we'll do this one a little differently because really there's only one way with a just a couple of different options that this works. Um, and so I'm going to show you the way I've configured it and show you um, uh, the options that you may want to choose a little differently, but there's only a couple of them.

[4:03:47] Well, what I'm going to show you is the best practice, standard, guaranteed way that this will work. It'll save you a lot of headaches trying to figure this out on your own. So, we'll X out of here and we'll go to my policy I've already created. And if we go down, you can see the categories here, but it's easier to see

[4:04:18] uh from what I've configured anyways see them if we edit them to see which categories they fall under when you go to select this. So, let's go ahead and do that. So, we're going to go ahead and click on configuration settings and edit so we can see how I configured this.

[4:04:49] So, we'll go top to bottom as is actually necessary in sequence. Uh, clicking on the Bit Locker category, we'll see that we have to enable it first. So, it got required drive encryption as enabled. You do want to um disable allow warning for other disc encryption cuz if you don't do that, this will not be automated. Um it won't

[4:05:19] work. You would have to have user interaction and it just isn't going to work that way. um where the you know you'll get the user would get a a warning popped up um saying do you want to allow uh bid lock or dis encryption and it's actually going to fail even if they say yes. So that's very very important um to say disabled for allowing a warning for other dis encryption. allow standard user encryption.

[4:05:49] Definitely need that. Um because if you don't do that, when the user logs in um they won't have permissions for uh encrypting the drive. So you you need that to enable con configure uh recovery password rotation. Um if that's the security measure you need in place, that's fine. I don't configure it. It's up to you in your organization.

[4:06:20] So, let's go ahead and collapse the Bit Locker category. Once you do that, what you have to do is just configure how each one of the types of drives are going to be encrypted with Bit Locker. The operating system drives, the fixed data drives, and the removable drives. And that's what we're going to dive into next. And we always want to encrypt the operating system drives. You may not um

[4:06:53] even allow or have fixed data drives that are inside of your desktop or laptop, your workstations. So that might be something that you could disallow through a configuration policy altogether or it just may be something that you don't want to configure. The same thing with removable drives. Um it all depends on your corporate policies and how you

[4:07:23] want to handle those. But at a minimal you want to configure operating system drives. Um so if you don't want to uh configure fixed data drives and rubble drives at least basically disable those in the configuration. So expanding the category for operating system drives enforce drive encryption type. Yes. Enabled full encryption. I recommend this. You

[4:07:54] could do um I would never allow the user to choose the again you want this fully automated use space only. It's quicker. Uh but every time they use space it takes a little bit of time to encrypt it. So I I I typically do full encryption right off the bat. That way it doesn't have to redo it every time the user writes to the drive. It does take a little longer to for the initial encryption, but it saves you time in the

[4:08:24] long run. Um, so that's my recommendation. I almost always recommend to not require additional authentication at startup unless you're really in a highly secure environment where you have to enter a PIN or a password before the operating system loads every single time in the BIOS. Users will get really annoyed with this. But if it's a requirement, you

[4:08:54] have a uh compliance regulation that requires this, then you probably do have to choose this, enable it, and then choose all the options, you know, whether it's a startup key with a PIN and TPM and all that kind of stuff. Um, I leave it at not configured. Um, the options are pretty straightforward if you enable it. So, we're not going to go through all those options. So the next few options are um related

[4:09:26] to that. So I leave those not configured. Going down to use um enable use of Bit Locker authentication requiring preboot keyboard input on slates. I usually enable this for those tablets that may be disconnected from a keyboard. And you know, if if there's some reason that um Bit Locker

[4:09:59] goes into recovery mode and they have to enter the recovery key and they don't have a keyboard available or it just doesn't this the the the tablet or the Slate just doesn't have the availability of that. Well, you want to enable this so that they can just use onscreen keyboard. You definitely want to select choose how Bit Locker protected operating system drives could be recovered. Uh choose that to be enabled.

[4:10:30] You need to choose uh allow 256 bit recovery key and 48digit recovery password in order for those keys to be stored in Azure. The whole idea here is uh that we want to store those recovery keys and packages in Azure so that uh we don't have to manually record those and potentially lose those or not be able to locate those in case of

[4:11:00] uh a bit locker recovery being triggered by something like a hardware change or just you know hard drive corruption or something like uh and and not be able to recover um to boot uh Bit Locker to be able to boot back into Windows. I recommend allowing the data recovery agent is not required, but absolutely absolutely

[4:11:32] configure storage a bit locker recovery information to adds. Now, that's a bit of a n uh a misnomer because that is really um in in tune um active not just active directory it's uh azure active directory enter ID and in tune so you definitely want to

[4:12:04] select store recovery passwords only. And the next item, do not enable Bit Locker until recovery information is stored to ADDS for operating system drives. Absolutely. You don't want to encrypt this and find out you don't have the encryption key in Azure and in tune. You can find them in both places, by the way. We'll see that later when we we go through our demos. That is absolutely essential because

[4:12:35] then if you have a an issue with recovery and it didn't start to Azure then wow you've got an issue on your hands. Actually, the next one I need to change, you want to omit the recovery options from the Bit Locker setup wizard. That um again, that's you don't want the users to have to have any interaction with the the Bit Locker. So, you want to

[4:13:05] turn that on to true. Otherwise, it's not going to be automated and that can interfere or just potentially fail altogether. And then we've got save Bit Locker recovery information to ADDS for operating system drives. Set that to true. Again, we want that information stored in Azure Active Directory and Intune or better known as enter ID these days. So, we've also got configure preboot

[4:13:37] recovery message and URL not configured because it'll get the default one which in my opinion is fine which basically is if there's a problem and uh bit locker recovery mode comes into play. It'll give you the default message. you could as an option um enable it. And if you enable it, you've got some options here on on um creating a custom message basically. But uh I don't think it's really necessary

[4:14:09] unless you think that recovery message is not good and you want to kind of custom brand it for your organization to let the user know yes this is a legitimate you know and give them a little more information on on it than the generic um bit like a recovery message then you can go ahead and do that but I think the default one is fine so I don't do that and that is the most important part the operating system drive

[4:14:41] u configuration and that's and that's what we're going to go with. Moving on to fixed data drives. Um pretty much the same selections just for the fixed data drives. Um, I think the only thing that's different in here

[4:15:15] is this last one. deny right access to fixed drives not protected by bid locker. So basically what this says is if if they had a pre-existing fixed data drive like a D drive for instance a secondary hard drive in their workstation um and

[4:15:45] and they used to be able to save files there before Bit Lacquer had enforced encryption. um when this policy takes effect until it becomes encrypted they will lose the ability to write to that. So, if there's a problem with a bit locker encryption that they can no longer um write to it, but I definitely if you're going to have fixed drives at all in your environment, um definitely say leave that at enabled. Um cuz there might be a lot of corporate

[4:16:17] data files on there that you don't want. Let's say that it's a desktop or laptop where they could pull out the you know solidstate disc or you know an um NV RAM disc and attach it externally to another computer. If that isn't bit locker protected man they could they could hack that easily very easily. So, I I recommend even if it's only a few computers um that have that or if the

[4:16:49] user has an availability to actually open up the box and and put it another drive in there and store data on there, uh I would say I would say even if it's a possibility, you want to enforce that. And then we have removable data drives um for Bit Locker. That's Bit Locker to go, which basically you're going to plug in a USB um or flash drive, you know, Bit Locker

[4:17:22] to Go is going to enforce a password to open that drive and you would have to use that password if you move that drive to another computer. I mean, that's basically how Bit Locker to Go works. I enable the um bit locker on removable drives. Um I allow the users to apply it. Um enforce it. Uh full encryption.

[4:17:56] I do not allow the users to suspend that encryption. Um, and same thing, deny right access to that if it's not um, just like fix fixed drives if it's not Bit Locker protected. Um, and the last one is a little bit unique. Do not allow right access to drives configured underneath another organization. I set that to false. So, if the drive is already um encrypted with a third party

[4:18:28] solution, then well, I think that's fine. So, we'll go ahead since I made some changes to my policy. Next, save. And of course you can create different Bit Locker policies for different groups, but I would say probably you want to have a universal standardized Bit Locker protection um for all at least workstations in your organization. So let's uh that's it for um drive

[4:19:00] encryption. Let's go back to endpoint security and go on to the next one. Next, we'll take a look at EDR endpoint injection and response. Really not a lot to configure in there. If you don't know what EDR is, uh, just look it up. Um, it's basically just selections for enabling it and and how to onboard it. So, we'll go ahead and look at that.

[4:19:35] And I've already created a policy for that. So, we will take a look at that policy that I created and edit the settings. So, we can take a look at the settings. So really there's only onboard and offboard for the configuration package. It's for advanced threat protection. So

[4:20:07] we have to configure that underneath onboarding. And then I just leave the other ones. Uh telemetry and sample sharing to Microsoft is off. And that is all there is to EDR. just basically enabling it and onboarding it and assigning it to your groups. Pretty straightforward stuff. And moving down the list,

[4:20:40] the last one that we need to do a deeper dive in that we haven't already pretty much completely covered in the portal tour is attack surface reduction, also known as ASR. Again, if you don't know what ASR is, go ahead and do a little research on ASR. So when we go to create a policy, we're going to select Windows. We could

[4:21:11] do config manager for co-managed environments, but we'll assume that's not the scenario. And the only one that we really need to configure is uh attack surface reduction rules. Um, you could additionally do the other ones, but this is the main one that you need to do at a minimal level. So, we'll do this in our demo and obviously create take a look at it

[4:21:45] and you'll see all the different settings in here. But we'll take a look at the policy I've already configured to give you an idea of what I recommend for ASR. Um, but just uh you know again this is one of those ones that depends on your line of business applications and your compliance regulation requirements

[4:22:15] and um you know what's going to work in your environment. So you'd want to test this like if this is a little tricky because if you again you want to do it to a pilot and test group first that has all of the um applications and um configurations a test machine or a few test machines first and you may want to do different ASR policies and

[4:22:47] target different groups depending on the line of business applications. Because if you get too strict in here, you may actually cause problems with the applications and you may have to make determinations on uh security versus functionality um in your environment. So you you kind of have to be careful with this. Um, but I'll give you kind of a generic uh standard best practice look at what the

[4:23:17] basic settings that should work for most organizations um without uh risking the functionality for those applications. So, we're taking a look at my ASR rules and what what I've configured. And of course, this is for Microsoft

[4:23:47] Defender. It's not going to work with third party apps. Um, you know, so I've blocked execution of potentially obiscated, that's hard to say scripts. Again, remember you click on the information on each one of these or do additional research to find out what it does and potential risks. Uh when I say risks, I mean risks to you know production

[4:24:18] uh environment and in in limiting what the users can do. Um so I I do block that. Um a lot of these are not configured. Um I do block um JavaScript from launching uh downloadable executable content. You may have to consider that. Um you know typically your options are not configured, off block, audit or warn.

[4:24:52] Um, you know, audit is just going to be something that you can reference and monitor and see if there are risks in your environment from JavaScript with executable content. Um, but any of these uh have pretty much the same settings or warn like the user would get a warning like hey man this could be a risk uh do you want to do this? So each one of these is like you know this is one of

[4:25:22] those ones you're going to highly customize and you might have to do several ones and target several groups depending on the needs of the uh um you know the personas like might have for instance a finance department that has certain needs. Um you might have executives that has certain needs with their applications. You might have management, you know, not maybe upper and lower management and then just the general um

[4:25:56] um office population or administrative support or even shop floor workers. And so you might have have to have a different policy for each one of those and target each one of those differently. Um, so this one is not one that um is a one-sizefits-all. You you really have to um you really have to test this very thoroughly. So um my recommendation is is to have separate

[4:26:28] groups for each persona and have test um devices or users in each one of those groups. and um have, you know, each type of persona test those and you know, modify, remediate, and um ultimately pull those out. But I think I think you could have just one ASR rule policy,

[4:26:58] but you might need to modify it with several and target each persona differently because you might have, you know, a need for a instance a third party app that needs some of this stuff and they have to run that app and you have to accept that risk. Um, so anyways, um, you you can do exclusions. So you could have, um, an exclusion for those apps

[4:27:28] that need that and then just have one ASR policy. A lot of this is not configured. Um, but I do like to select Hold on a second. Yes, I had to reread that because it was a little confusing. Um, use advanced protection against ransomware. Um, block would use its best effort to block ransomware. So, this is a very important

[4:27:58] one. I think this should be on everything. Um, again, you can click on this and it tells you um tells you, you know, basically what it does. Um and and that's pretty much it for ASR uh just generally speaking best practice recommendations and standardization.

[4:28:28] So going back to endpoint security, this really concludes everything that needs a deeper dive that we didn't already discuss in the intoune portal tour. um at a complete level. So that completes this module. Let's move on to the next module. So in this module, we'll be covering uh Microsoft application management known as MAM.

[4:28:59] So let's go over to apps. and create a protection policy for applications. Just as a review with um applications, they're going to be siloed into either a work profile

[4:29:30] versus pro uh personal profile. If you're enrolling your device or if you're strictly just using ma'am, your applications will um will be siloed with corporate data into um its own application so that it can do things such as manage the flow of data between personal data and corporate data, copying and pasting, those kind of things

[4:30:01] where it can save corporate data. to iCloud or Google Drive, those kind of those kind of things. That's what that's what mam is designed for to protect your your corporate data. So, we're going to create a policy for that. Going to create and we will do one for Android in this demo. Give it a name.

[4:30:31] Click on next. And we have a few choices here. We can target to selected apps, all apps, all Microsoft apps or core Microsoft apps. Um so you want to choose appropriately obviously. Uh if you want some more information, you could click on um learn about assigning app protection policies and

[4:31:03] get some information on that. Most commonly, we're probably going to choose all Microsoft apps or core Microsoft apps. And then you'll see the other selections go away. If we go to selected apps, we can choose just uh selected apps. Like maybe we just want to protect for instance um Microsoft Word

[4:31:35] and click on that and then also protect uh let's say teams in the same policy and then just have a different policy for the other apps. It just really depends on which apps you want to protect and how you want to protect them, whether you need different policies for them. Uh but in this one what I'm going to select is I'm going to say all Microsoft core apps actually

[4:32:08] click on next because I want to protect all my Microsoft core apps and the office apps and those kind of apps um in the same manner with with a flow of data and all that kind of stuff. So I'm going to go ahead and do that. We will not go through every single setting in here in this app protection policy. Um, but I want you to get a sense of what you can protect in an app protection policy. And

[4:32:39] there's a few of them that I'm going to suggest you definitely would want to do uh configure, especially again if you have compliance regulations that you need to protect your corporate data with. So I typically say that you don't want to allow saving your organization data to Android backup services. That would be either personal b personal Android services. I mean that's that's losing uh

[4:33:09] leaking corporate data. That would definitely block that. Um send organization data to other apps. Typically we want to say policy managed apps. The policy managed apps are the applications that are um managed through this policy. Your um your applications that you specify in here. You can exempt I'm exempt certain ones by going into the exempt um category

[4:33:41] here. Save copies of org data. Probably want to block this too. And if so, you can say, well, wait a second. I will allow them to save to one drive for business and shareoint um but none of the other ones. For example, protecting your corporate data in your corporate environment. So, they cannot

[4:34:11] uh send copies of your corporate data outside of your corporate environment. Um, I don't typically deal too much with telecommunications data. Underneath transfer messaging data too. This is, you know, like if you clicked on a link that brought you to a messaging app or something like that. Um, you could specify any or specific a specific messaging app. So, like if you

[4:34:41] get an email and you click on a um hyperlink um for texting or phone or something like that, then you could you could specify that information. Um receiving data from other apps. Now, it's typically safe to um receive data from any personal app. So, typically I leave it at this. If you wanted to be really strict and didn't want to allow that, you could say policy

[4:35:11] managed apps so that incoming um copying and pasting and receiving data and those kind of things, I'm sorry, uh receiving data from other apps. Copy and pasting is separate. Um only can come from policy managed apps. Um typically I just think that it is all laps as far as receiving data. Um when I go down to restrict copy cut

[4:35:42] copy and paste between other apps um I say policy managed apps with paste in as my selection. Um, so what that says is you can only copy and paste to other policy managed apps, but you can paste in from non-p policy managed apps. Um, and what you'll see uh hopefully we'll

[4:36:12] get to this in the demo is that um if you try to copy corporate data to a non-p policy managed app, you're going to see when you go to paste it, it's going to say your company restricts this. It's a it's a way to restrict cap copying corporate data from your corporate app that's protected to an app personal app that's not protected because obviously you can't protect those personal apps. So this is uh this is where I typically set that at.

[4:36:45] Now remember we're talking about the applications not the device itself. This is not controlling the device. So I block the screen capture and Google Assistant on the corporate apps. Now, how does it know it's corporate app? Because you signed into that app with your corporate credentials. That has nothing to do with the user um doing screen captures on their own personal data.

[4:37:15] Um for Android, I do require encryption. On iOS, this is not an option because iOS data is always encrypted. Let's see. This next one's a little tricky. You have to think about conditional access policies. Sync policy managed app data with native app or native apps or add-ins. Uh typically I'd say to block this

[4:37:47] unless um you really are already having a conditional access policy which only allows um the Microsoft apps basically to um sync data through conditional access policy. Also, if um you have allowed the native mail app on iOS, I know we're looking at

[4:38:18] an Android policy, but similar thing on iOS, you may have to leave this as allow um and and configure your conditional access policies to um make an ex an exception to uh the mail app and block all other apps. I mean, you have to really plan this through. This is not just one of those ones that you're just going to hit block on and not consider uh repercussions and and how you want to uh

[4:38:48] allow users to use um apps because uh especially on the iOS devices, people are so used to using the native mail app, it can really cause a headache for you um with your, you know, customer base, your users, and you're going to get a lot of push back. Um but you may be an organization that can just say um too bad. Especially if you're corporate devices then then you really have a lot

[4:39:18] more um control over this and you can say well you know this is what we do as a corporation. It's corporate devices blah blah blah. So enough about that. Printing organization data um up to you. You might want to block it. Um if if they can print it, they can scan it. You know, they can um take a screenshot with their phone and then send it off with their personal phone. You know, it's uh again, how strict do

[4:39:48] you want to get? Is it a BYOD device or is the corporate device? Those are all considerations into these kinds of settings. This next setting is uh web content transfer like hyperlinks and those kind of things. is whether you want to force uh it to open in Microsoft Edge. Now, on a mobile device, you're going to have to push Edge as an app uh in order to enforce this. If you say Edge um or an

[4:40:20] unmanaged browser, if it's an unmanaged browser, then it can be any unmanaged browser um or by the ID. So, um, you could say, well, it it only can go to Microsoft Edge or on managed browser and then you have to put in the browser ID and name of all the browsers that you want or just don't restrict it. Um, I guess

[4:40:52] the the thought process here is is some browsers are more secure than others. um you know with with with uh you know what can leak out of the browser. So this next setting has to deal with connected devices such as wearables. Do you want to allow um notifications to go to those devices? Do you want to block it altogether? just block organization data or allow

[4:41:25] and then you can start a tunnel connection on the app launch. Um, typically I just leave that alone unless your organization needs to enforce an encrypted tunnel like a VPN connection on the device. Um, but in this case we're not going to do that. Then we'll click next and we get into access requirements. Now remember this is access requirements for the corporate apps themselves, not

[4:41:55] for the device. This becomes especially important when we're dealing with BYOD and you're not controlling the device itself. If the device doesn't have any PIN requirements or timeouts or anything like that, it's left open indefinitely. Well, you probably want to in either scenario. Um, if you're just using MAM itself and not enrolling the device or where you can manage the device, um,

[4:42:25] you're in either scenario, you're going to want to make sure that um, there's a certain amount of security over the app itself. so that if the device was left open or stolen or lost and let's say they could somehow get into the device, well then there's going to be a secondary um requirement to get into the app after a certain amount of time. And that's what we're looking at here. These are PIN requirements um in the first part here for the

[4:42:56] corporate apps themselves. And again, corporate apps are the apps that are defined when you log into those apps with your corporate credentials. So, for this demo, I'm just going to I'm going to require it uh numeric uh simple pin allow. Actually, I'm going to block simple pen. That'd be like 1 2 3 4 0000. No, don't want that. Um,

[4:43:26] maximum or minimum pin pin length four digits is fine. You could some some organizations go to six, which is fine. I'm going to leave mine at four. Biometrics uh instead of pin. I usually allow that. That's fine. Um, you know, you can read through all this, but um override biometrics with pin after timeout. Um, that's fine. And I think most of this you can just leave at um the default

[4:44:01] pin reset after a number of days. Probably a good idea to do that. Um, and then you know specify the number of days on that and then you could say well they can't reuse the last three pins um for security purposes or just leave it at zero um or just one. I mean, if you left it at zero, it it

[4:44:32] doesn't make any sense to have a pin reset because it could reset it to the same one. Um, so you you want to put something in there. So, here we're saying still enforce the app pin even if the device pin is set. Some organizations say, "Well, if they got a device pin, then I'm not going to uh require them to have the

[4:45:04] app pin." But it really depends on whether your your organization is controlling that device and setting the requirements on the device pin. Because if not, I mean, you got somebody says, well, you know, I have a timeout of 24 hours for my screen lock and doesn't require a PIN. Well, let's say that device gets stolen and then there's no app PIN. Well, shoot, they can give you corporate data for a whole 24 hours. So,

[4:45:35] I always leave that at require unless you're controlling the device as a corporate device and you've already configured the corporate um device pin to what what you want. Then you can say, okay, well, we've got the device pin, so we don't need the app pin. Uh work or school credentials for access. I obviously that not required. We got a pin. I don't want them to have to put in their username and pass or

[4:46:05] just to get in the app every time it times out L and recheck the access requirements after X number of minutes of inactivity. That means if the the app is open, you know, and it's inactive, um, force force a re recheck of the credentials with a pen. So, I think I'll leave it at that. So now we've got a really cool feature underneath conditional launch. Um you

[4:46:36] can change the values on these. So basically it says after five uh uh pin um attempts and they failed. What do you want to do? So you could change it to 10 or whatever. You could reset PIN. You could wipe the data from a device. That's a corporate debat. uh corporate uh data not the device itself. You're not doing a factory reset. Remember this is all with corporate data on the applications uh

[4:47:08] inside the corporate applications. Say offline grace period um 1440. Uh that must be uh yeah that must be minutes I think. Let me double check that. Oh yeah it says block uh access minutes over here. Um so if it's offline for 1440 minutes which is 24 hours then

[4:47:44] block access or you can choose what data um days but uh not sure why that's grayed out honestly. Um, all they have to do is reauthenticate. Yeah, I'm sorry. We've got one for black access and one for wipe days. That's why cuz we did it in the previous um the previous screen. And all they have to do is

[4:48:15] reauthenticate. And um if they were blocked because of the the 24 hours, they just have to enter their PIN. If they're blocked for being offline for 90 days, then they will have to um you know reauthenticate with their credentials. The data would have been removed from the device, but as soon as they reauthenticate, then with their username and password, then the data will come right back. It's

[4:48:46] not like it's wiping the data from their account. And then you have some additional um options here that you can choose if you want to. Um highly recommend keeping uh the jailbroken rooted devices block in the Samsung Knox uh device attestation which would be rooted. Um, I'm sorry. Uh, just that it's a Samsung

[4:49:18] Knox uh capable device. If it's not, then block access cuz you don't want um devices that you can't control. But is if it's just ma'am and you you're not actually um able to control the device, it's BYOD, then you might want to um remove this one for Samsung Knox because

[4:49:48] not all um Samsung's are going to have Knox on them. And if you're allowing BYOD, then you might not have a choice. Um, but I would definitely say, well, if you're bringing BYOD, we won't allow you to h access our corporate data if you're jailbroke uh if you got jailbroken or rooted device. You just it's part of our corporate policy. Sorry, but find another device or reverse the jailbroken rooted um

[4:50:19] functionality on the device if you want to access corporate the data on your BYOD device. highly uh highly recommend keeping that. Now, there's a whole bunch of other ones you can add in here. We're not going to go through any of those. Um but um whole bunch of other ones you can add as far as you want to access our corporate data on the corporate apps. Well, then here's some other restrictions that we're going to apply is we can't enforce those in

[4:50:51] your device through Ma'am, but we're going to do a compliance check and make sure that your device passes these basic compliance checks in order to get access to your corporate data on your BYOD device. or it could be corporate but uh corporate devices we would normally deal with a compliance policy through MDM and not through ma'am. Um so that's that

[4:51:21] we're not going to do any scopes to further define um filter based on different criteria. We're not going to do that. Um, we will add groups later when we go to do our demo. So, we're not going to add it now. But again, you know, test with a pilot, don't roll it out to production and have everybody screaming at you cuz something doesn't work or they're locked out of something. Always do pilot and testing before you roll out

[4:51:53] to everybody in production. And then when you do it in production, roll it out in batches. Don't roll it out to everybody at the same time. So, I'll assign that that later. We'll click next. and create. And we're good on that part. So now we're moving on to ma'am configuration profiles.

[4:52:26] When we go to create a new configuration profile, we have two options. We can do it per managed devices or managed apps. And it's going to be uh pretty much a completely different um type of configuration based on on which that we select. So, do we want to create a configuration for the app itself or the device? So let's take a look first at managed apps.

[4:52:56] We'll give it a name. We've got to select the app. So in this case, we'll say Outlook. Uh select which platform. Click on next. There's no settings catalog available for this. So, we're going to have to go in and choose the settings individually for the app that we want to configure

[4:53:26] from the settings underneath each category that's available. So, just taking a look at this example, we have general configuration settings. We could manually enter those tunnel, you know, whatever. not really important for Outlook. We're pretty much uh going to focus on the configuration settings if that were our application. Um all the settings that we want to push to the

[4:53:57] application so the user doesn't have to configure it for themselves. For instance, focused inbox, biometrics, contacts, can they save them or not? Mail tips blocking external images default app signature configured yes or no um replies all the configurations that Outlook has if you want to uh predefine

[4:54:29] those for the application when you push uh when you push the application and they'll be uh configured shortly after the application is pushed. So all these kind of settings um for the application itself we can define in a configuration uh profile and so per application each one of these it's going to be different depending on the applications and the settings available for that application. So,

[4:55:01] we'll get out of this and we'll take a look at creating um a configuration profile for managed devices instead of the apps. And what does that look like? So, we have to give it a name. Choose the profile platform. the profile type, let's say fully managed, dedicated or

[4:55:32] corporateowned. And then we'll select in this case um which one of the applications we've already uh got assigned or pushed and we'll click on next. And we're going to select configuration designer. I don't want to do a whole JSON file on my own. So depending on the app, you may have uh some selections

[4:56:02] that you can do from the settings catalog itself or you may just have um JSON selections that you can choose and kind of edit manually. So in this case for this app um we have to go to the JSON editor through the configuration designer and not just JSON file. So for instance we could say prefill in shared

[4:56:35] device mode um suppress camera consent for QR code. hit on those. And then what we're going to see is we will be able to fill in that information um and choose um uh whether it's just a checkbox or

[4:57:05] whether we have additional selections here. whether we have to type in a string or a variable or etc or just a an onoff enabled or not configured type of uh scenario. It it depends on each app and each configuration for that app that we choose. Um, and so that would be a view from

[4:57:35] the configuration designer with the JSON selections. So, let's get out of this. Let's take a look at a little different one. Of course, the app has to be pushed to the device for these configurations to take effect um or be at least available. And so with the device ones, when you're creating a device uh manage device uh configuration

[4:58:05] profile, you're not going to see that app available to configure if you haven't already created that app ahead of time. So keep that in mind. So let's take a look at the smartung I'm sorry Samsung smart switch that I already created a configuration for that app. Now I've already I've already created that app and that's why it was available to configure. What did I do in there?

[4:58:42] So very similar to what we just saw, I said use configuration designer instead of entering manually JSON data. Um, and so I chose, um, I could add a few of them. Uh, but in this case, there's really only one selection for that app. Allow the smart switch run. Yes, no, yes, or no, basically. And when I click on that to be available,

[4:59:12] spoolean, I had to actually click this to make it true. Otherwise, it's not going to configure. very important when you're doing this. Some of these have checkboxes. If you don't do the checkbox, the boolean is going to be false and it's not going to run. And so, um, here's my selection. Uh, enable, uh, users to connect this app across work and school profiles enabled. This is one of those ones that's a

[4:59:42] little tricky because if you don't do this for this app, it doesn't work um, even in the work profile. Um, and so this is one of those ones that we had to do in app configuration um, profile inside of MAM. And that's pretty much all there is to the configuration profiles and MAM. So that finishes up this module and let's move on to the next one.

[5:00:16] In this module, we'll be covering application deployment for iOS, iPad OS, Android, and Windows. We'll begin with iOS, iPad OS. So we'll go to apps and then underneath apps we are going to see platforms and for each platform we can click on

[5:00:48] each platform and create apps underneath each one of those platforms. So, let's go to iOS, iPad OS. And before we go any further, I do have a whole separate video on this with a demonstration. So, uh this is pretty simple, pretty straightforward. We'll be going through it pretty quickly. Check out the link below for my uh separate video on doing

[5:01:20] this. Oh, and also do not forget that you cannot manage or deploy apps to iOS iPad OS until you've created that Apple MDM push certificate. If you have not already watched the part of this video where I go over the creation of that certificate, it's at 3 hours, 1 minute, and around 55 seconds. Definitely watch

[5:01:50] that if you haven't watched that yet. That is a prerequisite. All right. So, let's continue. So, we will go to create and then select app type iOS store app. Select. And then we're simply just going to click on the search the app store. Uh, iOS is real easy to do. So, let's click

[5:02:20] on that. Clicking on search the app store. And we're just going to simply type in the name of the app we want to find. So, for instance, Microsoft Word. We'll click on it, select, and pretty much everything is going to be filled out for you, even the icon.

[5:02:50] You could uh fill in the additional stuff if you wanted to. Um, but it's pretty much next, next, and then assign as you would typically assign first to a pilot test group and then to um production after that. And keep in mind once you uh create the app you can create a configuration profile in ma'am for the app if you

[5:03:20] needed to. And there's really nothing else to creating an iOS iPad OS store app. So let's move on to the next type of app. So let's now go to the Android um application deployment types and click on that. And when we click on create,

[5:03:51] we're going to have a couple of different options in there and we'll discuss those. We have options for Android store app and manage Google Play app. For men's Google Play app, we will have had to already configured the connector

[5:04:22] um to uh our men's Google Play Store. And um if you haven't already seen this part of the video, it's at uh 3 hours, 8 minutes, and approximately 22 seconds. Um so review that. And of course, I've uh went a little more in depth with uh a separate YouTube video that I have on this um and so check out the link below on that.

[5:04:55] But when we go to create, we have two different options in create. One of them is for an Android store app and one of them is for a manage Google Play app. The manage Google Play app is going to require that uh connector and the manage Google Play app is also

[5:05:25] going to require that the device is enrolled either as a BYOD or the corporate device and in tune. So, if you're doing ma'am without enrollment, um you have to choose the Android store app because the managed Google Play app will not work if you're just using ma'am without enrollment. So, we will first go through a manage

[5:05:57] Google Play app and then an Android store app. So once the connector has been set up for the uh managed Google Play Store, it's really easy to create that uh type of app. So we'll go ahead and create that right now. We simply select uh managed Google Play app and click select.

[5:06:30] We will search for that app on Google Play. Then we'll click on it. And then we're going to have to click on where it says select. And once we click on select, we're going to then have to click on sync. And then we'll give it a few minutes.

[5:07:01] And after we click on sync and it will show up in our Android apps. Once we see it in our app list, we will go ahead and click on that and then go to properties so that we can edit the assignments.

[5:07:32] down below. And we can either require this app for certain groups. We can make it available for enrolled devices or make it available for enrolled or non-enrolled devices.

[5:08:03] And this is the same type of assignment that you'll see for any type of application iOS, Android or Windows. So in this case, I'm going to go ahead and add this as a required application to a certain group. Go ahead into that group and assign it. And once assigned, you'll see it in the

[5:08:34] included um underneath require. Remember that if you're going to require an app assignment, that device has to be enrolled within tune. It can't just be using um ma'am without enrollment. So there is a different type of Android app that you can deploy. called the Android Store app instead of

[5:09:06] uh deploying it from the manage Google Play Store. It's basically just a link to the regular Android store where they'd have to click on it. And the use case for this might be that you don't want to link um a connector to the manage Google Play Store. or the second one probably the most often is that you're using um EYOD apps um with ma'am without enrollment where you're not

[5:09:37] managing the device and you have to deploy the Android apps this way. This is a little more involved but it's not too bad. We're going to go to create. We're going to select the app type as an Android store app. Select. And now the most important information we have to gather is

[5:10:07] the app store URL. We have to gather this URL for the hyperlink for the app that we want them to be able to click on to install themselves. um it'll still make it available and in ma'am without enrollment um it'll still launch the company portal app in a manner that will just manage the app for corporate data without enrolling the device. So you would still want them to

[5:10:37] uh get this app push as an Android app instead of them just going there and to the app store and doing it themselves. It's much more convenient this way. In order to grab that app URL, we're going to have to go to play.google.com/store slapps and search for that app to begin with.

[5:11:13] We will find the app and click on the app. And what we'll do is we will grab the URL from uh the the store location where we found that app just simply from the web browser um address bar. Then we will go back to

[5:11:43] our app, our Android app, and we will paste that in the App Store app uh section. And we'll give it a name, Microsoft Excel, and fill out the rest of the information. We can choose to show this as a featured app. Let's go ahead and do that. And um the rest of it is uh optional. I

[5:12:14] would select an image. So, let's go ahead and do that. Typically, I'll just grab that image from the Google store and copy that image and save it as a PNG for um import uh into the um into the app. So, let's go back and add that logo.

[5:12:44] And that's kind of important because it seems legitimate uh when the user is going to click on it and it'll just look ugly if it doesn't have that. And then you're just basically going to click on next. Um next assignment. Um, if we're going to do this for ma'am without enrollment, we'll go ahead and say add group. Get our group

[5:13:19] and create. We're going to get have to give it a minute or two before it shows up and then we'll see it show up. Notice here we have one that is the one we just created our Android store app for Excel and then we have one we created for the manage Google Play Store app.

[5:13:52] So, you're probably wondering if my device is not enrolled, it's BYOD, and it's uh ma'am without enrollment, how are the users going to get apps delivered? Well, that's a great question. On their device, they're going to go to the web version of the company portal app. So, that address is portal.mmanage.microsoft.com. So, they go to web browser on their device

[5:14:22] and then they're just going to log in with their corporate credentials. any apps that you have designated as featured apps will show up underneath featured apps and then any other apps will show up underneath uh recently published apps. But if the there's not enough space then

[5:14:54] the user simply clicks on all apps to see all the applications that are available. So the idea here is that if they click on one of their corporate apps like Microsoft Excel and click on view and store, it'll simply have a click on install straight from the Android store

[5:15:28] without having them have to find the app and install it and all that kind of stuff. So we'll let that install. Then once installed they'll click on open and it's starting to configure.

[5:16:00] And if they've already um successfully authenticated um to to um corporate you know the corporate enterprise Microsoft 365 with another app then uh it should just automatically log them in like you see here and have a list of you know all their documents and all that kind of stuff and they're done. If not, they'll have to authenticate for the first time to, you know, their corporate data with their username and password. And then

[5:16:31] they'll uh within a few minutes, they'll get an a prompt for the company portal app, not to enroll, but just basically to um allow it to manage that app. And that's it. To wrap up our app deployment module, we are going to now dive into uh Windows apps. Before we get knee deep into it, there's

[5:17:01] a few things I want to mention. First of all, I have a whole video dedicated to this. So, check out the link I provided right here. Second of all, we are not going to go through app packaging in this um in this video. It's in the video that I provided. I go through app packaging step by step in order to do what we call a wind32 app. And don't let that name fool you. Even though it's called a

[5:17:31] wind32 app, it's also 64bit application. you need to create a package through a command line utility. Um, and again, that's covered in the the video that I provided here. And when packaging, you're always going to want to have the MSI file, not an .exe file. Uh so that's my little bit of information before we get into actually

[5:18:02] deploying um Windows applications specifically when 32 apps is what we're going to focus on in this um demo. So we will go to windows on these platforms and then again this is getting very familiar to you. Create we will select the app type as

[5:18:38] a Windows 32 app down here underneath other. Now, notice there are Microsoft Store apps for Windows. Uh, we won't go over that. They're pretty easy. You basically, it's it's just like the Google Store. You just select it from the Microsoft Store. Um, but or web application link, uh, Edge, Microsoft 365 apps if you want to deploy Microsoft 365 apps, but they're all so

[5:19:09] straightforward. is really not even worth going over. Um, we want to focus on the one that's going to be a little bit um challenging to uh to understand and a little bit more involved. So, we're going to do uh you know deploying actual Windows apps on a Windows computer. So, we're going to select Windows app 32. Win32. We're going to hit select.

[5:19:39] And now we come to the part that says where is your package file? Okay, so this is the process that we're not going to go over in this video. Again, check out my video on Win32 apps. I go through all the steps of creating that package. And again, when you create that package, you want to create that package with an MSI file. And you'll see that in my my other video. So we want to select the app

[5:20:10] package file. We want to find that package that we've created. So we're going to click on the folder to find that. And once we find that app with the intoune win extension, um it'll tell us the name, the platform, the app version, the size, all that kind of stuff. So this is the package file

[5:20:40] that we need to upload into in tune in order to um deploy this app to Windows machine. So we'll hit okay. We're going to have to edit this information to what we need to do. Um, can edit the description, um, or just leave it generic like like the title. It's up to you. You do have to, um, this is sevenzip. Um, so I'm just going to say sevenzip is the

[5:21:10] publisher and the app version. Leave it at that. And you'll see why in a minute. Um, you could say this is a a featured app, but 7zip probably not a featured app in my opinion. Could fill out the rest of the stuff, but not necessary. Browse for the logo. Hit okay.

[5:21:43] And then we'll just click on next. And here's all the important stuff. You really want to pay attention to the details in here. So from the MSI file, it's going to pick up on the install command the default switches from the MSI file. Now, you may want to modify that according to um some customization that

[5:22:13] you might need to do for the installation. And you'll want to look up the um vendor's documentation on this to see what those switches are for that MSI file. Um it's just really dependent on the MSI file itself and the vendor. Um but you may need to add some additional switches on this one. Uh the I switch just says install and it's shows where the MSI file is. I think Q is for quiet. I think uh N is for no prompt. I don't

[5:22:43] know. Um, the other nice thing is from an MSI file is it automatically picks up the uninstall command from the MSI file. So, you don't have to try to figure that out on your own. You'll want to consider how long you think this would take to install and um put a reasonable amount of time in there and maybe give yourself a little bit of buffer so that you can

[5:23:14] give a reasonable timeout if it fails and not wait forever. Scrolling down a little bit, if we hover over allow available uninstall, it says select yes to provide the uninstall option for this app for users from the company portal. Select no to prevent users from uninstalling the app from the company portal. So, if it's a required app, I would say no.

[5:23:47] If it's just something that's optional, well then maybe we just leave it on yes. Install behavior always leave it at system unless the vendor says it has to be installed under the user context. You don't want user interaction. You want this to be automatically installed um from in tune. Um I pretty much never see that an app has to use has to install underneath the user context. If it does,

[5:24:19] then you have to do your research. Um, but always leave it underneath system for all apps unless specifically required by the vendor. Under device restart behavior, there are a few options, but I typically say app install may force a device restart. Now, if you're in an environment where you don't want users to just get an automatic restart

[5:24:50] without warning, well, then uh you may want to change these options. And here's the options that you have. I leave the return codes at their default unless you need to add or change the return codes um for your specific needs. Um but um I would leave them at the vendor

[5:25:21] defaults unless you have a specific reason to change those. So we click on next and now we have the requirements uh for the app to install. If we set the requirements too high, the app will not install. And a bit of advice, even though the vendor documentation says for instance it needs 64 GB of RAM to install and hard drive space and blah blah blah. And if the system does have

[5:25:51] that, I've seen this fail in the past. I typically do not set the requirements on this except for you have to select something uh for the minimum. So starting with check the operating system architecture um I would typically just leave it at no. It's up to you. Um, on minimum operating system, I would probably leave that at

[5:26:24] um the minimum Windows 10, even though Windows 10 is going down to support. Um, that's up to you. Those two are the only two that are required to select. The rest of them are not required. And let me scroll down a little bit. So I would say for the rest of them just leave them blank. It the the application itself is smart enough to know that it doesn't meet the minimum requirements.

[5:26:55] So there's no need to go into here and and select those. Um, again, I've seen it fail where you set the minimums and even though the operating system or the the device has those minimum requirements, there's something quirky about it. So, I tend to recommend not setting these. So, we'll go ahead and click on next now.

[5:27:26] And the detection rules is basically how do I detect if this application already exists in the version that I'm deploying on this this the the system that I'm deploying it to. And so we have several options underneath here. Well, at least two options. If it's a mainstream wellestablished um application,

[5:27:57] you're almost always going to select manually uh configured detection rules. If it's some weird uh you know third party app that was customdeveloped for some specific reason and they just don't follow the the rules. um then you might have to have a custom detection script. But um in most cases, we're just going to say manually uh configure detection rules to see if that

[5:28:28] application already exists um for the version that we're installing. So when we go to add the rules to detect whether that application is already installed in the system, that's where we're going to have a few options. Most often we're going to choose MSI. Um again, if you choose to use an EXE,

[5:28:59] that's your only option. And you've got to look for the file um or registry key. And that file could be an actual file or a folder. We'll see that in a second. Um well then you've got to go down that path. But if you, and this is why I say always try to get an MSI cuz if we choose MSI, it's automatically going to populate um depend uh you you know um

[5:29:32] from the MSI that we've loaded what the um MSI detection code is. We could say version check yes on that and say greater than or equal to. But if the application itself the MSI product code changes from version to version we do not need to select the product version check. So let's say

[5:30:02] sevenzip uh changes their product code from one version to the next. We don't need to do this. If they don't, then we'll have to go in here and say, well, okay, um, you know, greater than or equal to and the version number, something like that. We're going to choose no. Let's say that we didn't have an MSI and we wanted to uh validate by file.

[5:30:35] Then we have the option to specify the path and also either a file or a folder. And then the detection method would be um uh either file or folder exists date modified created string size of megabytes all those kind of things. Um so you can detect um so for instance sometimes the vendor will have different installation paths

[5:31:06] or different um uh executables or MSIs for different versions um or just you know not even different versions but that that that application exists in that uh in that path. So we could choose file and we could also choose registry key path value name texture method key exists key does not exist string comparison version

[5:31:37] comparison integer comparison I mean really you need to look this up um depending on the app uh a bit beyond the scope of of just in tune training that we're doing right here um but know that those are all available. So, we're we're going to go with the MSI. Uh we're going to skip the product version check. We're going to assume that each version of the application we're doing right now is going to change

[5:32:07] the product the product code changes between each one of those versions. So, it'll be able to detect the version um by the product code. We're going to hit okay. And by the way, you can add more detection rules if you wanted to. We'll hit next to go on to dependencies. Now, the important thing about this is let's say we had .NET Framework um you know 4.8 as a dependency

[5:32:39] or any other type of dependency. When we go to add, we would already have to have created an application for those dependencies in in tune to be able to add them. So, it's only going to list what we have um in in tune already as an application to be able to specify the dependency. So, if we didn't create that ahead of time, we cannot specify dependencies for this application. So again, go to your

[5:33:11] vendor, say, "Are there any dependencies and figure it out?" If it's not part of an automatic Windows update that most computers will have, then you may want to create an application just for that dependency and then add it underneath dependencies. But we're going to say no to this one. We're not going to add anything. We're going to click next to get to super seedments. And this is going to become important as you continue to roll out new versions of

[5:33:41] applications. Um, I chose this spec specifically because I do have an earlier version of sevenzip that I want want to supersede. But when you read this whole thing right here, it basically explains everything to you and you could click on learn more. Um, when you supersede an application, you can specify which apps will be directly updated or replace to to update an app. Disable the uninstall um previous version option. To replace

[5:34:13] an app, enable the uninstall previous version option on the app that you had already deployed. So, you have to make sure you do that. Um, pretty much that's it. So, I'm going to go ahead and click on add. And I'm going to do, as you see here, the version I have uh that I'm trying to deploy right now is 24.09. There's an earlier version of 23.0

[5:34:45] 1.00.0. And so I'm going to say uninstall that previous version. Now, if you have several versions, you're probably going to want to create an app for every single version. that's in your environment and specify those when you select them as super seeds so it can uninstall those. And then importantly, you're going to see uninstall previous

[5:35:15] version. Yes, we want to uninstall the previous version unless it's an upgrade and and it's only an upgrade and it's not um a full install. And so we click on that and we've gotten through all of the hard stuff. Now it's just pretty much next. Uh scope tags, we're not going to deal with that. and then add in group. And again, you

[5:35:47] know, you're going to want to pilot this, test it before you roll it out to production. Make sure you, you know, have a test machine that has previous versions on it thoroughly. Test it before you roll it out to production. And that's it. That wraps up not only our um section on win32 app deployment but also our module on app deployments. So let's move on to the next module.

[5:36:20] So we are at a very great point right now. We've went through the uh in tune portal tour. We've went through pretty much all the uh major configurations uh for policies and enrollment and all that kind of stuff. Now we need to talk about what are the common mistakes and best practices recommendations for in number one is a big one lack of clear

[5:36:51] planning and strategy. I mean this is I I can't emphasize this uh enough. This is really important from the incipiency of the project. We need to involve all stakeholders. That may be management, that may be the network team, that may be uh the desktop deployment team, that might be

[5:37:22] the security team, that might be the network team. We have to involve all of them in the discussion and planning. The mistake is jumping straight into configuration without defining user cases, user device groups, and management goals. and planning this properly. Quite honestly, the impact is it leads to inconsistent policies, device management gaps and difficulty

[5:37:52] scaling later on. The second common mistake is to uh utilize poor group and assignment design. For example, using overly broad or overlapping groups for policy and appmens. The impact could be you would have conflicts between policies and profiles.

[5:38:22] Uh for example, configuration profiles, policies, uh duplicate uh app deployments and trouble shooting headaches. Um the best practice is to use dynamic groups with well-defined filters if possible. Next is misconfigured compliance policies and we spoke about this a lot. Um really compliance policies is a minimum set of let's get us through the

[5:38:53] gate uh gateway to get us uh to authenticate to our corporate apps and then after that let's define our uh device restriction policies and all that kind of stuff. Um uh setting compliance policies are too strict or inconsistent uh across platforms may cause a problem with them even getting into the corporate apps to begin with um impact uh which we started to talk

[5:39:26] about. um devices may become non-compliant unnecessarily blocking users and increasingly uh causing help desk calls. The next one is a big one. Ignoring conditional access testing. You really need to test the conditional access policies before rolling them out. So the mistake is deploying conditional

[5:39:56] access policies to all users and devices without stage roll out or exceptions. Impact is users can get locked out of critical apps and services which is critical to your um production environment. It's just really bad to not uh plan this properly and um pilot it and test it first. Best practice is to test with pilot groups be before enforcing organi

[5:40:28] organizationwide. So scrolling down a little bit next is not planning for hybrid aad join scenarios with azure ID/raure ID. Um, and this is particularly um relevant to autopilot.

[5:40:58] Do you have remote users that will not be joined to active directory and will not be hybrid and some that will be joined to active directory and hybrid or a combination of the both? It's really crucial to planning. So one of the mistakes is assuming all devices will be Azure AD joined or hybrid joined um when some of them will be one or the other or maybe

[5:41:28] uh both. The impact is that device devices fail enrollment or duplicate devices appear. Best practice is to plan and identify device join strategy carefully. You really need to uh look at the personas in your organization. Who's going to be remote? Who's going to

[5:41:59] be joined to active directory? Who's going to be hybrid? All those kind of things. The next one is overlooking app deployment planning. The mistake is deploying too many apps at once or not categorizing apps required versus available. The impact is slows enrollment, network congestion and user frustration.

[5:42:30] Best practice is to phase app deployment and prioritize business critical apps first. Next is not using autopilot properly. The mistake is failure to capture proper hardware hashes or configure profiles directly. So this is very important. we spoke about earlier in this video

[5:43:00] um you know requiring the the device uh I'm sorry the um the devices manufacturer vendor to register those devices in in tune or manually entering those in uh in in tune for autopilot now and again I have a whole separate video on hybrid um autopilot is uh a lot more

[5:43:30] complex and and again refer to my video on that. The impact is devices fail out of the box experience uh provisioning OB or end up unmanaged. Best practice is to validate autopilot profiles and tests with autopilot before scaling. And if you're in an environment where you have both hybrid autopilot and

[5:44:01] uh just pure joined Azure AD entra ID uh autopilot devices. Well, then you're going to have separate profiles for those policies, and you're going to want to test both those. So, let's scroll down a little bit more. This one is often overlooked, but it's very important. The lack of communication in user

[5:44:32] training. Users have no idea what's going on. We have to develop a plan and we have to communicate that plan so they know what's going on. Whether it's a corporate device or a BYOD device, they have to have um step-by-step instructions. They have to know what's going on, what's controlled by the organization and what's not controlled by the organization. And it's totally dependent on your uh

[5:45:03] device deployment scenarios. And you might have a se several of them. You might have corporate devices and B yod devices. So you have to plan for that appropriately. So the mistake is not informing end users about what will happen to the devices. The impact is users will perceive into as intrusive leading to resistance and increased uh support tickets.

[5:45:34] Best practice is to provide clear instructions in documentations and FAQs for enrollment or if it's just a B yod with ma'am without enrollment those instructions as well. Another uh mistake um that I see all the time is poor policy naming and documentation. Uh and the mistake is random naming

[5:46:05] conventions and undocumented configurations. You want to document all of this. Um the impact is it's difficult to troubleshoot, audit or delegate management. Um best practice is to use standardized naming conventions and um uh auditing. Well, that will impact auditing and allow you to oh delegate.

[5:46:35] The next big mistake is ignoring endpoint security config integration and we have a whole module on this a whole section on this. Anyways, um this is very very important. So the mistake is not configuring in tune endpoint security policies. That's defender, ASR, attack surface reduction, EDR, those kind of policies. Um, uh, Bit Locker, those kind of things. You want

[5:47:06] to configure those. As we have discussed in this video, the impact is that the devices may be managed for compliance but lack the security that you need for your organization and possibly ultimately your sec security compliance uh regulations that are demanded by your industry. Best practice is to integrate into with

[5:47:38] defender for endpoint or your third-party security tools as we talked about with the connectors and uh detection uh customized detection u rules and etc. So, scrolling down a little bit more. Another common big mistake is

[5:48:08] overlooking reporting and monitoring. Um, not reviewing in tune reports or alerts regularly. Now this could be on the application level or the security level or the device level but uh you need to monitor those. Um the impact would be issues like failed enrollments, non-compliance and app deployment failures go unnoticed. So you really need to do as a best practice monitor in

[5:48:40] tune dashboards and proactive alerts. And the next one is huge. We've talked about this incessantly throughout our training. No pilot or staged roll out. A mistake is deploying configurations to the entire organization without piloting or testing. You really have to deploy to small groups, test and

[5:49:10] validate before going on to production. The impact is that organizationwide outages or broken workflows could happen. Best practice is to always start with a pilot group or test group, whatever we want to do, and validate before expanding to uh production. So, scrolling down a little bit more.

[5:49:42] Uh, this is a big one too. Mismanaging BYOD versus corporate owned devices. This impacts um compliance policies and configuration profiles and ma'am all that you want to configure your enrollment profiles, your configuration profiles, your uh compliance policies and your MAM

[5:50:12] policies uh specific to corporate and personal/BYOD devices and plan that appropriately. The impact is privacy concerns, excessive restrictions or lack of control if it's BYOD uh with corporate devices specifically. So, as I've already alluded to with the

[5:50:44] previous mention, use different compliance profiles and enrollment methods for VYOD versus corporate devices and also um you know configuration policies as well. The next one is failing to plan for multi-platform support. We've talked a lot about this, so um I think you get the point. um already about this but mistake is not

[5:51:14] accounting for differences between Windows, Mac OS, iOS and Android with the compliance configuration and all that kind of stuff. Impact is that policies fail or don't apply correctly and the best practice is to create platform specific configurations and test separately. But I think we've uh done a good job at uh illustrating that already. And the last one is not keeping up with

[5:51:46] Intune and policy changes. Whether that's compliance policies, uh, configuration policies or MAM policies or MA configurations in tune uh, it changes all the time and um, especially in a hybrid environment where you have active directory some of the GPUs um, uh, ultimately will um, be able to be accommodated in in tune um, even if they weren't able to be done so

[5:52:18] previously. So keep up on that. Um so mistake is using outdated methods such as relying on ADGPOS only uh or not enabling uh new intoune features. The impact would be missed opportunities for simplification and improved security. And um I will add to that um moving towards um

[5:52:49] the ultimate goal of relying less on Active Directory and more on Intune for the future may be all intoune. Uh but you're probably not there yet. So this goes without saying that us as IT consultants or IT pros, we constantly have to stay updated with the technology and in tune changes all the time. So keep updated on uh Intune's monthly uh

[5:53:20] feature uh update releases. So from my experience that's a pretty comprehensive checklist of common mistakes and best practices uh to be aware of. So that would uh wrap up this module. Let's move on to the next one. So now we will cover tips and best practices. There will be a little bit of

[5:53:52] overlap from the previous module on best practices, but it doesn't hurt to uh reinforce some of these major uh considerations with best practices. Number one on the list, planning and strategy. And this is extremely important. I can't reinforce this enough. Define your goals and use cases first. for example, BYOD versus corporateowned, app management versus full device

[5:54:23] management. So, plan meetings with stakeholders and team members. And these team members typically are your security team, your application owners, uh network team, uh the desktop support team, management, executives, all those people who have a a stake in the roll out of intoune. Always start with a small pilot group

[5:54:53] before rolling out to all users and devices. And additionally, I say start with test users and test devices, not even um real production pilot users. Separate policies by platform and purpose to avoid conflicts and simplify troubleshooting. Helps you isolate and target where the issues are. Document and standardize naming conventions for all profiles, policies,

[5:55:24] and groups. Number two, device enrollment and group management. Use dynamic Azure AD groups where applicable uh based on operating system, ownership type, and department for example. And you can use those for automatic targeting and applications, policies, profiles, all those kind of things.

[5:55:56] plan B yod personal devices versus corporate enrollment strategy separately. For example, company portal for BYOD. We already talked about um ma'am without enrollment autopilot. You may want to have separate autopilot policies for uh different uh types of uh device enrollment strategies.

[5:56:28] Leverage Windows Autopilot to streamline new device provisioning and test enrollment scenarios again before rolling out hybrid join Azure AD join and personal devices before you roll out to the whole entire enterprise. Number three, policy configuration and compliance.

[5:56:58] Keep your policies modular and specific. For example, one policy per function. Bit locker, anti virus, ASR, password, Wi-Fi, and on and on. Use compliance policies to enforce security standards. for example, encryption, OS version, jailbreak, root detection.

[5:57:29] But remember, compliance policies on their own will not enforce anything without a conditional access policy that says you're going to block them if the device is not compliant. Keep that in mind. Apply conditional access policies in stages and always test with test or pilot groups first. Don't just roll out a whole bunch of conditional access policies to your entire organization.

[5:58:01] You're going to have a nightmare on your hands. If you are enrolling BYOD personallyowned devices, avoid overly restrictive settings on those personal devices to prevent easer frustration. Number four, security and data protection. Enable Microsoft Defender for endpoint integration for advanced

[5:58:31] security and monitoring. Uh we went over this earlier in the video. Use app protection policies ma'am for BYOD scenarios to protect corporate data without full device management/enrollment. We talked about this a lot with the MAM protection policies and we even talk about MAM without enrollment. Um, so we spend a lot of time on this implement device encryption. Bit locker

[5:59:03] for Windows, file vault for Mac and secure boot where supported. Configure attack surface reduction ASR and endpoint detection and response EDR for Windows devices. And we did spend a bit of time on this uh as well in the endpoint uh security component leverage conditional access policies. I

[5:59:33] can't say this enough. Conditional access policies appear in in tune but really they're outside of intoune. in Entra um SLAure and um uh they come into play for for many things that go hand in hand or integrate with Intune for instance requiring MFA locking legacy authentication protocols uh things such as blocking outside of the US um but conditional access

[6:00:04] policies you can't really deploy in tune without planning additional access policies. That's going to be necessary. And scrolling down a little bit. Number five, application management. Categorize apps into required,

[6:00:36] available, and remember with available we have available for enrolled devices and we also have available for enrolled and unenrolled devices such as unenrolled would we uh would uh mean devices such as BYOD that are only using MAM policies and uninstall groups for clear deployment strategy. Deploy business critical apps first

[6:01:08] during enrollment to minimize easer downtime. Use the company portal app for a user self-service app installation. So that could be a fully installed uh version of the company portal app where the device is enrolled or it could be the web version of the company portal app that we talked about for ma'am without enrollment for devices that are BYOD and they do not enroll into int.

[6:01:42] consider using the wind32 app packaging for complex app deployments with dependencies and superseded and we we spent quite a bit of time on that. So if you missed that, check out that section in my video. Number six, monitoring, reporting, and troubleshooting. Regularly review intoune reports. These could be enrollment failures, compliance, app

[6:02:13] deployment status, uh device statuses, all those kind of things. Set up alerts and automation for non-compliance or failed enrollments. A little bit beyond the scope of what we're covering here, but you can always do the research on that. Monitor the security dashboards in Intune and Defender for potential threats. That's a big one. And that'll give you information on how to remediate

[6:02:43] and what those threats are. and use endpoint analytics to assess device performance and proactively fix issues. Again, we didn't go into much detail on that. Um, but it's a tip and uh a little bit beyond the scope of of this video, but um you know uh definitely look into that and do some research in that. Number seven, user communication and

[6:03:14] training. This is often overlooked but is extremely crucial and it is imperative for a successful roll out in a production environment. Notify users well in advance before deployment to explain what will change and why. Whether it's corporate devices or BYOD, you still need to notify them of the changes, what those changes will be, and

[6:03:45] why those are happening. Provide clear enrollment instructions if it is a device that's going to be enrolled, including screenshots or videos. Even if it you're using ma'am without enrollment, you still want to have uh screenshots and videos. educate users about privacy boundaries, what it can and cannot see on their devices. And Microsoft has a lot of

[6:04:16] information on their documentation uh that you can just basically provide URLs or grab the screenshots from uh and to create those that documentation or do both uh grab some of the screenshots that are um c customized for your environment and then provide the links from Microsoft. That's typically what I do and offer self-help resources and FAQs,

[6:04:46] frequently asked questions to reduce support tickets. It's also helpful to provide the support information, uh, help desk, um, phone number and email address for anything that wouldn't be covered um, in those resources. Number eight, maintenance and continuous improvement. Now, we all know that Microsoft changes things all the time. We have to as IT professionals in a

[6:05:19] supportive environment keep up to date and keep our um policies and profiles up to date as well as um keeping our communications up to date to the corporate uh users. So we need to regularly review and update policies as the OS and Intune features evolve. We need to decommission unused or de

[6:05:50] duplicate policies to reduce conflicts. We need to stay up to date on Microsoft's monthly intune feature releases. We should conduct periodic audits of devices compliance and security posture. Microsoft does provide a su a secure score analysis in the defender portal

[6:06:20] and it provides all the um remediation that needs to be done. So, um, if you don't know or are not familiar with the Microsoft secure score and the defender portal, take a look at that. Um, it's a very helpful tool on the dashboard to tell you where your weaknesses are, where you can improve and recommendations on how to pro improve that, uh, etc. So scrolling down a little bit more.

[6:06:59] Number nine, governments governance and role delegation. Use rolebased access control arbback which uses the lease permissions model to delegate in tune admin tasks appropriately. Microsoft has documentation on the different intoune roles and I recommend using PIM

[6:07:29] privileged identity management to assign these roles and I have a whole separate video on PIM and that's how I recommend assigning these roles. So check out my video on PM which goes handinhand with the se second bullet point. Separate global admin duties from day-to-day device management to reduce risk um to the corporate environment.

[6:08:00] Enable audit logs to track policy changes and administrative actions. And that's a pretty simple task. You can just do a Google search on that in the tenant and it'll show you how to enable the audit logs. Pretty pretty straightforward. Number 10, cloud and integration considerations. Integrate with Azure AD, now known as Entra ID,

[6:08:31] identity protection for riskbased conditional access. Again, beyond the scope of this video for Intune, but definitely a a tip and recommendation. Just check out the documentation for Microsoft on that. Use intoune plus defender for endpoint for unified endpoint prot uh security protection. We talked about this a few times. I'm not going to kill that one.

[6:09:02] consider co-management with configuration manager SECM uh which is known known as MECM during phase migrations. Um and again there's a lot to that. So uh check out my YouTube page. I I probably will have a video dedicated to this uh shortly in the future. There's a lot to that but

[6:09:32] basically there's uh in phase migrations there's connectors to Azure um and federation that happens that you know connections to the tenant and and um and that provides a federation all that kind of stuff but then you also have workloads and you slide the workloads to which workloads are going to happen on uh SECM and which ones are going to happened in Intune

[6:10:02] and uh you know for instance uh compliance versus configuration and um along with that there's group policy versus uh in active directory versus um the policies you set in in tune all that kind of stuff and also plan for third-party app integration. You want to have conversations with the vendors.

[6:10:32] Um any uh business critical apps, line of business apps, for example, Cisco VPN, any other VPN apps, um all that kind of stuff. You need to plan for those. So in summary, the key takeaway is a successful intoune deployment combines very careful planning, testing for test groups and pilot testing,

[6:11:05] user communication, and continuous improvement. I can't stress that enough. Intoune is not something that you set and leave alone. you're going to constantly be modifying uh monitoring and improving it. Always validate before scaling and leverage in tunes reporting and security integrations to stay proactive. So that finishes this module on tips and

[6:11:38] best practices. Let's go on to the next module. So now that we've configured and assigned policies, let's take a look at them from the device side on both a Windows and Android device as demos. So beginning with Windows, we will go to devices,

[6:12:12] then go to Windows and choose uh one of the devices from the list that's enrolled and policies. these are assigned to. And on the overview category, notice at the top we have a bunch of

[6:12:42] options for enrolled devices. We can retire the device which will remove it from in tune but keep the device intact. We can wipe the device uh give it a fresh uh restart. Um we can delete the device which will delete it from intoune and entra ID/asure

[6:13:12] ID. We can sync the device to sync the policies and applications to the device to force it to uh process a little quicker. We can restart the device, collect diagnostics, do a fresh start, which will give us a couple of options on whether we want to keep uh user files or not and keep it enrolled in in tune.

[6:13:42] And then we have a few more options available underneath the ellipsus at the end. And those are all pretty self-explanatory. a lot of stuff with uh Defender if you're using Defender. Um, rename the device from here, but we'll show you in a second. You can rename the device in a different location, locate the device if that has that capability, and um, you know, run remediation that's

[6:14:12] in preview mode. So, those are options from the ellipsus. Notice also um at the essentials um section you have all the summary information. You have listed the ownership. You can see it's corporate. It's a corporate device. device name,

[6:14:46] who it's enrolled by, um who the primary user is, um whether the device is compliant or not, and some other stuff. Last check-in time. Some really important summary information in here that you can get all of it at a quick glance. When we click on the properties category,

[6:15:16] we're going to be able to see some of this information we see here, but also have the uh ability to change it. So, just a a few quick things in here. Um, you can rename the device from here, which is very convenient. Um, you can change uh the device ownership from personal to corporate or vice versa. Typically, you're only changing it to corporate from personal,

[6:15:46] but you can change it right here. You can also change the primary user when the device is reassigned. Uh typically though you would go through a computer refresh and that that user would um sign into the user but it might not change the primary user when you do that anyway. So you might have to change primary user or also remove the primary user.

[6:16:17] Um very important things to understand that you can do from here. If you have created and assigned a properties catalog configuration policy when you go into resource explorer you will see all sorts of information on the system. Uh ton of stuff. Now, this does take up to 24 hours. And unfortunately, um I did assign this,

[6:16:48] create the policy, and assign it, but I haven't waited 24 hours. So, uh I'm not getting any information yet. So, it it can take up to 24 hours for that info to sync. Um we'll see at the end if it comes in. Um not too important that we actually see the information, just know it's there and how long it takes. Uh but some really helpful information. So um again you have to create a properties catalog configuration policy

[6:17:20] and assign it and then you'll get this information within 24 hours. But you will get the hardware information right off the bat without having to configure any sort of policy. So we can click on that. This happens to be a virtual machine, so it's going to be pretty generic in my scenario. Any apps that are discovered will show up underneath discovered apps.

[6:17:55] Does a pretty good job at that. And their versions, uh, very great way to actually, uh, check on a a device. um even apps that you didn't deploy through in tune. So that's uh a really nice feature. And then the next two categories are really um the most important for what we've deployed for policies uh both compliance and configuration to

[6:18:26] check on the status of those um whether they you know were successful um or failed or whether even recognizes that they got assigned at all. So let's go into device compliance and take a look at which uh compliance policies uh we see there. The default device compliance policy will always show up. Any additional

[6:18:56] compliance policies that you have uh configured and assigned for that device or user will show up. Additionally, now it's important to understand that if you have created a conditional access policy that says the device has to be compliant, every single compliance policy that you have assigned has to pass compliance.

[6:19:27] Otherwise uh the conditional access policy will block um access to the whatever applications are in there in the conditional access policy which are typically the Microsoft apps. So they all have to pass if you are using a conditional access policy that says in order to get access to the corporate apps uh it has to pass compliance uh policies.

[6:19:57] If we click on these we we can get some more information. So, we see all the settings in this basic compliance uh custom policy that I have configured and it says that they're all compliant. Uh but if for some reason one of them failed um it would it' show you that and you could click on it and find out uh you know some more information why it failed.

[6:20:27] clicking on the default one. Um, what you're really looking at is does it have a compliance policy assign and is it active and no enrolled user exists. Um, if it doesn't have a compliance policy assigned, then you're going to go back to your other compliance policies and say, "Oh, did I forget to assign it or is the user or device not in the right group for assignment?" Those kind

[6:20:58] of things. Taking a look at the device configuration policies. It's going to list every single uh configuration policy that we have uh assigned to either the user or the device through a group or through all devices or all users. And we can click

[6:21:28] on any one of those again and we can take a look at each one of the settings to see what failed or succeeded. So let's say that we went to uh Bit Locker Windows and it said that it failed um for the system account or the user account. We'd go in here. We'd click on whichever setting had failed. and we'd uh click on it to get some more

[6:22:00] information on that. But in this case, I've made sure that I've set up everything correctly so that they all pass and I have none that are failing. So, there's really nothing to um to troubleshoot in here. Moving down to recovery keys. These are the Bit Locker um recovery keys and packages that we

[6:22:31] said had to be stored in Azure Active Directory before the drive is encrypted. We can click on show recovery key and underneath show recovery key we can unhide it. where it says show which is not really that necessary. The most important thing

[6:23:02] is to copy it to clipboard so that if there is a triggered Bit Locker recovery during boot where the computer cannot boot without the recovery key, you can copy to clipboard and then copy and paste to a text editor of your choice and you've got the Bit Locker key to provide uh during uh the recovery process.

[6:23:33] So if we simply paste into there, we've got the recovery key. So it's very important that you validate that these um you know these that the bit locker has um has actually uh the the policy is actually applied through the device configuration but that you also got the recovery key and you can copy and paste that. It's a very

[6:24:04] very important thing because you don't want to lose um access to that drive to boot the operating system. And you know even though we redirect folders and map drives and all that kind of stuff, the user always has a tendency to store files in weird locations and if they can't access their their drive then they they lose them. So very very important

[6:24:37] And we scroll down to managed apps. And these are the apps that we have deployed through in tune as opposed to discovered apps which just grabs everything that is already installed on the device. So we'll take a look at that. It's going to list um all the applications that you've deployed and assigned to that computer either through

[6:25:10] again all devices, all users or a group that includes the device or user. Um, and if you don't don't see the application that you think should have been installed, then you've got to go back and look at the um application deployment and um take a look at the assignments. Um, notice I've got two in here um

[6:25:42] underneath the intent, the resolved intent. That's kind of important because one of them I have as a required install and one of them I have is available if they want to choose to install that. Um so underneath the installation status you see that the Microsoft emulator says available for install and the company portal app says not applicable. And I'll

[6:26:13] explain that the company portal app is not applicable because I was sick of waiting for the company portal app to install through intoune for the demo. So I installed it manually on the uh the computer and that's why it says not applicable. But if we actually clicked on that, what we're going to see on any of these is a checklist of all the steps that it goes through. So let's say that one failed

[6:26:43] um an application failed. It's going to give us a a checklist of all the steps that went through and it's going to give you more information on the failure steps in the error code. So very important to know that you can check this uh for any uh application that fails or is in a pause state or something to find out uh what's happening with that application deployment to troubleshoot it.

[6:27:18] under enrollment. When we click on that, we can see uh the enrollment state and we can see how it was enrolled. So this um this device actually was enrolled through autopilot as a hybrid join device. And yes, I have a whole separate video on autopilot with hybrid active directory and entra ID/Asure ID

[6:27:50] enrollment and that whole procedure. So you can check out my video on that. So that's pretty much all the major stuff looking at the Windows device from the intoune end. Let's take a look at the device um from the actual device end within Tim. So we triggered a bit lack of recovery so we can show you what that's like.

[6:28:23] And there's only a few things on the computer end, the device end in Windows that I want to show you. So, if we go to the start menu and we search for worker school and click on access worker school.

[6:28:58] You'll notice two accounts over here on the right hand side. If your hybrid AD Azure AD joined one for entra ID Azure AD and one for your active directory domain. If we click on the ETRA ID and click on info,

[6:29:30] it's going to give you all the information on the synchronization and connection to um Entra ID for this computer. And if we go to the sync button, we can force a sync between uh this computer and enter ID to get the latest policies and everything else synced up. We can also create a report to send for

[6:30:02] uh diagnostic information to our IT admin. So, we've got couple of different options in there. We're going to go ahead and click on sync and let that run for a little while. This can take several minutes. And then when it finishes underneath device sync status, it'll tell you uh the last attempted sync was successful and the date and time. If it was if

[6:30:33] there were an issue uh a problem, then it would tell you that it failed and uh you would have to probably create a report or do some more advanced um diagnostical uh troubleshooting like looking at log files. So, we can create the report by clicking on create report and then it tells you where it's going to go. And then you would just export

[6:31:05] and then go to that um location to grab the um export to hand to your IT admin. And it's that simple. So you're probably wondering where those log files are for the sync. If we open up file explorer and we type in this location right here,

[6:31:38] we will get to the log files. So, we'll go ahead and hit enter on that. And there are our log files. So if we are a technician, we could open those ourselves, take a look at them, see what's going on, or we could hand hand those to um our technician for

[6:32:12] troubleshooting purposes. This is especially important um and specific to the um sync agent and uh syncing the policies and all that kind of stuff. And lastly, let's take a look at the company portal app on the Windows end. So, this is the home screen.

[6:32:45] We also have the app screen. We've got downloads and updates screen. If there's any available downloads and updates, we have uh a list of all of our devices for who we're signed in as. Then we've got help and support. That'll

[6:33:15] give us help and support information for our organization. Now that we've given it some time, I did want to jump back really quickly and just take a look at the resource explorer. It had populated the information. Remember I said it could take up to 24 hours, but it's only been, I don't know, maybe eight or so hours. Now, this is a virtual machine, so it's not going to have a ton of information that uh a you know, a physical machine

[6:33:47] would have. But if we take a look through some of this information that's gathered, um, really nice information here. It's gathered my BIOS information, CPU, disc drive, encrypt, uh, encryptable volume, all that information, logical drives, memory information. Of course, that's dynamic memory that I've allocated on

[6:34:19] my virtual machine. Network adapter, all the information on my network adapters, operating system version, the build number, install date of the build number, there's no SIM information, system enclosure. I don't think that's really um relevant since it's a virtual machine, but it's giving me some generic information. Time,

[6:34:50] time zone, TPM. It's using a software TPM, the Internet of Things, video controller information, um, Windows QF information, the, uh, quality features, um, which, uh, hot fixes were installed. A lot of really great stuff here from the resource explorer. So,

[6:35:20] that really wraps up our demo on Windows. Next, we're going to go uh jump right into the demo for Android. So now let's take a look at the intoune side of the Android configuration, the compliance policies, the configuration profiles and all that kind of stuff.

[6:35:52] And you'll see in a minute that we're actually using in this demo a by yod a personally owned device with a work profile. So let's go ahead and take a look at devices. And underneath devices, let's go to Android.

[6:36:23] And this is an enrolled device.

[6:36:59] So on overview that category on the left hand side we still have a lot of the same options that we saw in Windows on the top uh but not quite as watch. There's of course retire, delete. There's an additional one for remote lock. So, if I were going to pull in

[6:37:32] my screen of my Android device that's managed as an enrolled device and hit that remote lock. Let's see what happens. Let's click unlock. Let's go back to my device. and give it just a minute. And voila, the device is locked. The

[6:38:03] remote lock worked because it's enrolled. Even as a personally owned device, remember we have a certain amount of control over the device when it enrolls. So, I'm going to have to unlock this device to get back into it. Um, we can also do a sync reset passcode. And here's a cool one,

[6:38:36] send custom notification. So, if we do that, let's see what happens. So, I have um given it a title and a body and I'm going to push send. And let's see what happens on the device when I do that. There we go. We get it. We get a

[6:39:06] notification on the device through the company portal app and it pops up in our toast notifications and it'll tell us um uh the message from the company and we can click on it um for more information. So that's a pretty cool feature when your device is managed even as a BYOD personally owned device when it's

[6:39:36] enrolled. When we go to properties, we still have a little bit in there that we can configure, but not so much as a BYOD device. We cannot change the device name as we could for a corporate device. We can however change how that shows up in in tune underneath management name.

[6:40:12] We can change the device category and the device ownership. However, if we go to corporate, I suspect I've never done this full transparency that on a BYOD device, it's going to prompt that user device for permissions to allow that device to be changed to corporate. So, we're going to leave that

[6:40:42] as personal. And because it's personal, we can't change the primary user um or remove the primary user. So, moving on to hardware. Very similar to what we've seen in the Windows demo. Going to give us all the hardware information. Good to know.

[6:41:15] underneath uh discovered apps, anything that's on that device, regardless of what we have deployed to in tune. And this is curious. I just noticed this. Um maybe on BYOD it cannot grab all the applications. Um not sure. Have to look that one up.

[6:41:45] Maybe in the comment section. Leave me a comment and we can discuss this and investigate a little bit further. Um I have not noticed that before. Just as in Windows, the two big ones are device compliance and device configuration. And that's where all your policies that you push are going to show up. So, taking a look at device compliance first.

[6:42:18] Again, the default device compliance policy is always going to be there. And if we've done our compliance policy settings correctly, we're going to require an an assignment of a compliance policy. So, I've got one that I've assigned called Android personallyowned compliance. And remember, just as in Windows that we've reviewed already, every single compliance policy has to be

[6:42:48] compliant. If you're going to enforce compliance through a conditional access policy for access to your corporate apps and thus your corporate data, if we're to click on one of these uh especially the one that I configured with custom settings, we would see more information. every setting that I required in this custom compliance policy will give me a state

[6:43:21] and if there's a failure then I could click on it and get some more information but they're all compliant. I made sure that this would all work. And looking at the default compliance policy, what we see is yes, it has a compliance policy assigned, is active, and enrolled user exists.

[6:43:55] Next is device configuration. These are our configuration profiles policies. And so we will see any configuration policies that have been applied to either the user or the device. If we click on the policy, we will get some more information

[6:44:27] on all the settings inside of the policy that have either succeeded or failed. And then you could click on each one of those settings, of course, to get uh some more information on what happened along the way and the steps along the way. And lastly, clicking on managed apps, we see all the apps that we've deployed

[6:44:58] either to all devices or all users or specific groups that include specific devices or specific users. And of course, um, just for this device or this user, um, we're going to see the apps that are deployed to this device, depending on the user that is on this device or the device itself. Of course, we're going to want to make sure that all the applications that we

[6:45:29] intended are either available or have been a required install. So um we could check out the version of course but the resolved intent tells us whether it was just available or required and then the installation status tells us whether it's installed or not. So for instance, we have an available

[6:45:59] without enrollment that's installed. We have an available without enrollment that's not installed because a user just simply chose not to install it. We have a required install that's installed. and then another one with the same thing uh available installed with all enrollment and not installed.

[6:46:31] So if there's required apps that are failing then what you need to do on the required install is to click on it and look at the steps along the way and determine where it failed. And I'd just like to illustrate one last thing on BYOD devices specifically with

[6:47:01] the personal and work profiles. You will see at the top here separate tabs for work and also for personal profiles.

[6:47:39] So if you switch between you will see which apps are protected with your work profile and which apps are protected or are not protected and are in your personal profile and have uh zero control by your corporation. I do realize that this video has been

[6:48:12] extremely lengthy, but I wanted it to be as comprehensive as possible. Please check out my other videos on my channel. Hit the like button, subscribe, and click on alerts for notifications on new video content. Feel free to share my channel or any video content. It does help out immensely. Leave a comment and I'll try to reply as

[6:48:42] best I can. Good luck on your Intune career. This does wrap up our Intune video guide.
