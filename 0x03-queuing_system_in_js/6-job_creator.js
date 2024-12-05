import { createQueue } from 'kue';

const queue = createQueue();

const jobData = {
  phoneNumber: '1234567890',
  message: 'Hello, this is a notification message!',
}

const job = queue.create('push_notification_code', jobData)
  .save((err) => {
    if (err) {
      console.error('Failed to create job:', err);
    } else {
      console.log(`Notification job created: ${job.id}`);
    }
  });

job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', () => {
  console.log('Notification job failed');
});
