import { AbsoluteFill, useVideoConfig, interpolate, useCurrentFrame } from 'remotion';

export const MyVideo: React.FC<{ text: string }> = ({ text }) => {
	const frame = useCurrentFrame();
	const { fps } = useVideoConfig();

	const opacity = interpolate(frame, [0, 30], [0, 1], {
		extrapolateRight: 'clamp',
	});

	return (
		<AbsoluteFill style={{ backgroundColor: 'black', justifyContent: 'center', alignItems: 'center' }}>
			<div style={{ opacity, color: 'white', fontSize: 60, textAlign: 'center', padding: 40 }}>
				{text}
			</div>
		</AbsoluteFill>
	);
};
