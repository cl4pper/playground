import React from 'react';
import useFetchComments from './useFetchComments';

const Container = () => {
	const { data: comments, isLoading, isError } = useFetchComments();

	if (isLoading) {
		return <>Skeleton</>
	}

	if (isError) {
		return <>Error card</>
	}

	if (!comments) {
		return <>No content</>
	}

	return (
		<ul>
			{comments.map((comment, idx) => (
				<li key={idx + comment.postId + comment.id}>{comment.email}</li>
			))}
		</ul>
	)
}

export default Container;
