function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw(new Error("Jobs is not an array"));
  }
  
  for (let jobber of jobs) {
    let job = queue.create('push_notification_code_3', jobber);
    job
    .on('complete', () => console.log(`Notification job ${job.id} completed`))
    .on('enqueue', () => console.log(`Notification job created: ${job.id}`))
    .on('failed', (err) => console.log(`Notification job ${job.id} failed: ${err}`))
    .on('progress',
	    (progress, data) => console.log(`Notification job ${job.id} ${progress}% complete`));
    job.save();
  }
}
export createPushNotificationsJobs;
