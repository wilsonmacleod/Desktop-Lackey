import axios from 'axios';

export default class POST {
    calendar(task) {
        const url = `/Calendar/${task}`;
        return axios.post(url, task)
    }
}