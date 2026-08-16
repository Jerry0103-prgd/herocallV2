interface LogoProps {
  className?: string
  size?: number
  style?: React.CSSProperties
}

export function Logo({ className, size = 32, style }: LogoProps) {
  return (
    <img
      src="/hero-call-icon.png"
      alt="HERO CALL"
      width={size}
      height={size}
      className={className}
      style={style}
    />
  )
}
