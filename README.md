# Designing for Offline Use: App for Information Access in Rural India

India has many welfare programs aimed at supporting different sections of the society. Two of the largest welfare programs are the National Rural Employment Guarantee Act (NREGA) and Public Distribution System (PDS). The former aims at livelihood security by providing at least 100 days of wage employment in a financial year to every household whose adult members volunteer to do unskilled manual work [1]. The latter distributes subsidized food and non-food items to India's poor [2]. While both of these programs are well intentioned, there are many accountability problems in them. One of the biggest challenges is the lack of awareness of these programs. And even after workers enroll in the program, they may not get their dues because of petty corruption or delays due to errors .

With the numerous problems in the welfare programs, Civil Service Organizations have stepped in to help improve accountability in the program. This has been aided by two developments in India:

Right to Information Act 2005: Under this Act, any citizen may request information from a public authority which is required to respond within 30 days. The Act also requires public authorities to computerize their records for wide dissemination [3].
Ubiquity of mobile phones: India's mobile base accelerated rapidly, standing at 1.035 billion as of June 2016 [4].
One such effort is the Combating Corruption with Mobile Phones Project, led by Vivek Srinivasan of Stanford University [5]. The project has led many interventions in Andhra Pradesh, Chhattisgarh, Bihar, Maharashtra and Telangana. Some examples are:

Problem: NREGA workers were being underpaid. Solution: They instituted a voice call to subscribers with the amount of wage that has been paid to the family.
Problem: Payment intermediaries hoarded wages for months, when they were required to pay in 4 days. Solution: They monitored the date of credit by the government and the date of disbursement. If payments are delayed, then they intimated the authorities.
8 months back, we joined the CCMP team as volunteers. Our goal was to build an application which can store and display NREGA transaction data as well as update them. The application was to be used by karyakartas (social workers) to verify with workers whether their details are correct. The main requirement of the app was that it should be able to work in areas with flaky or no internet. This is for reads as well as writes (the app should be able to save writes locally till it is able to sync with the remote database). The UI needed to be very simple so that it could be used without any additional training. The hope was that in the long run, NREGA workers will be able to access this information and take corrective action.

The following are the different components of the app:

Ionic
Our first choice was whether to build a native app or a web app. Native apps have many features such as push notifications, offline mode, load on the home screen etc. Compared to this, mobile web apps accessed in mobile browsers lack most of these features and feel like lesser versions. Unfortunately, most of the social workers had phones which were running extremely old versions of Android. We decided to use the Ionic framework. This allows you to build progressive web apps and native apps with one codebase. This also has plugins like Cordova which help you port the web app to a native app. This made a lot of sense since we were a team of 3 who were working on the project part-time.

Ionic also allows you to build progressive web apps. This allows the mobile app to behave like a native app. This was particularly useful for the offline mode feature. The key technology behind progressive web apps is a service worker. These are scripts which run independent of the app in response to events such as network requests, push notifications, connectivity changes, etc [6]. Here is an example of a service worker that interprets fetch events and returns data from a cache if a network request fails.

Firebase
The next choice we had to make was on the datastore. All the NREGA payment reports were crawled daily and stored in a remote MySQL database by the CCMP team. The first option we considered was using a local SQLite database to sync with the remote MySQL db. The main challenge with this was we had to build abstractions to sync data from the remote store to the local store along with the lookup logic when there is a network failure. Hence, we decided to go with Firebase which comes with offline capabilities. This works off the shelf with no extra lines of code. The Firebase Realtime DB automatically picks data from the cache when network is not there and refreshes the cache when network is available. This is not without limitations though. The cache size is limited to 10 MB. As of now, the amount of data required by the social worker is 2 - 4 MB. Also, we also had to sync between the remote MySQL and Firebase databases daily.

Demo
https://youtu.be/UjPffPKtv58

Future Work
As of now, we have synced the data for all districts in Jharkhand. The app is under user testing. In the future, we plan to explore PouchDB so that we can sync more than 10 MB. We are also exploring other interfaces like chatbots for the social workers to interact with the data.

If you are interested in this work and would like to contribute, please contact us.

This project was done in collaboration with Mayank Rungta, Karthika Purushothaman and Rajesh Golani.

[1] National Rural Employment Guarantee Act 2005 https://en.wikipedia.org/wiki/National_Rural_Employment_Guarantee_Act,_2005

[2] Public Distribution System https://en.wikipedia.org/wiki/Public_distribution_system

[3] Right to Information, Act 2005 https://en.wikipedia.org/wiki/Right_to_Information_Act,_2005

[4] India's mobile user base touches 103.5 crores http://www.ndtv.com/india-news/indias-mobile-user-base-touches-103-5-crore-telecom-regulator-1456845

[5] Combating Corruption with Mobile Phones http://cddrl.fsi.stanford.edu/research/combating_corruption_with_mobile_phones

[6] What is a progressive web app? http://blog.ionic.io/what-is-a-progressive-web-app/

