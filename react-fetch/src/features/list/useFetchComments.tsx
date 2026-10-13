import { useEffect, useState } from 'react';
import { URL } from '../../constants/urls';
import { Comment, FetchResponse } from './types';

const useFetchComments = (): FetchResponse => {
	const [isLoading, setIsLoading] = useState(false);
	const [isError, setIsError] = useState(false);
	const [data, setData] = useState<Comment[] | null | undefined>(undefined);

	const fetchData = async () => {
		setIsLoading(true);
		setIsError(false);

		try {
			await fetch(URL).then(async (res) => {
				const payload = await res.json();
				setData(payload);
			}).catch(() => setData(null));
		} catch (err) {
			console.error(err);
			setIsError(true);
			setData(null);
		} finally {
			setIsLoading(false);
		}
	}

	useEffect(() => {
		// fetch data from endpoint
		if (data === undefined) {
			fetchData();
		}
	}, [data]);

	return {
		data,
		isLoading,
		isError
	}
}

export default useFetchComments;
