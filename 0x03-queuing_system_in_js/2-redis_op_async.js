import {createClient, print} from 'redis';
import {promisify} from 'util';

const client = createClient();

client.on('error', err => {
	console.log(`Redis client not connected to the server: ${err}`);
}).on('connect', () => {
	console.log('Redis client connected to the server');
});

function setNewSchool(schoolName, value) {
	client.set(schoolName, value, print);
}

const get = promisify(client.get).bind(client);
async function displaySchoolValue(schoolName) {
	const value = await get(schoolName).catch(error => {
		if (error) {
			console.log(error);
			throw error;
		}
	});
	console.log(value);
}

displaySchoolValue('Holberton');
displaySchoolValue('Holberton2');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
