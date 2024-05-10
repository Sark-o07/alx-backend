import {createQueue} from 'kue';
const queue = createQueue();
const job = queue.create('push_notification_code', {
	phoneNumber: 'string',
	message: 'string',
}).save(error => {
	if (!error) {
		console.log(`Notification job created: ${job.id}`);
	}
});
job.on('complete', result => {
	if (result) {
		console.log('Notification job completed');
	}
}).on('failed', errMessage => {
	if (errMessage) {
		console.log('Notification job failed');
	}
});
