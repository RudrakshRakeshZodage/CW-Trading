import { Composition } from 'remotion';
import { MyVideo } from './MyVideo';

export const RemotionRoot: React.FC = () => {
	return (
		<>
			<Composition
				id="MyVideo"
				component={MyVideo}
				durationInFrames={1800} // 60 seconds at 30fps
				fps={30}
				width={1080}
				height={1920}
				defaultProps={{
					text: "Success with Crowd Wisdom Trading!",
				}}
			/>
		</>
	);
};
