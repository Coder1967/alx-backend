import 'kue'
queue = kue.createQueue();

var job = queue.create('push_notification_code', {
  phoneNumber: '6542343',
  message: "still there",
});

job
  .on('enqueue', () => {
    console.log('Notification job created:', job.id);
  })
  .on('complete', () => {
    console.log('Notification job completed');
  })
  .on('failed attempt', () => {
    console.log('Notification job failed');
  });
job.save();
