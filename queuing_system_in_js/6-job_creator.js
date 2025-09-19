const kue = require('kue');

// Create a queue
const queue = kue.createQueue();

// Job data
const jobData = {
  phoneNumber: '4153518780',
  message: 'This is a test notification'
};

// Create a job in queue named "push_notification_code"
const job = queue.create('push_notification_code', jobData).save((err) => {
  if (!err) {
    console.log(`Notification job created: ${job.id}`);
  }
});

// Event: when job is completed
job.on('complete', () => {
  console.log('Notification job completed');
});

// Event: when job fails
job.on('failed', () => {
  console.log('Notification job failed');
});
